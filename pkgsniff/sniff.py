import socket 
import os
import struct
from ctypes import *


#listenning host
host    =   raw_input(':: Type the listenning host IP ::')


#ip header struct
class IP(Structure):
    _fields_    =   [("ihl",    c_ubyte,4),
            ("version", c_ubyte,4),
            ("tos", c_ubyte),
            ("len", c_ushort),
            ("id",  c_ushort),
            ("offset",  c_ushort),
            ("ttl", c_ubyte),
            ("protocol_num",    c_ubyte),
            ("sum", c_ushort),
            ("src", c_ulong),
            ("dst", c_ulong)
            ]
    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):

        #map consts of the protocol to their respective names
        self.protocol_map   =   {1:"ICMP", 6:"TCP", 17:"UDP"}

        #Ip addresses legible to the human race ..
        self.src_address    =   socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address    =   socket.inet_ntoa(struct.pack("<L", self.dst))

        #protocol legible to humans
        try:
            self.protocol   =   self,protocol_map[self.protocol_num]
        except:
            self.protocol   =   str(self.protocol_num)



#create a pure socket and associate it to the public interface
if os.name  ==   "nt":
    socket_protocol =   socket.IPPROTO_IP
else:
    socket_protocol =   socket.IPPROTO_ICMP

sniffer    =   socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host,0))

#we want the ip headers included in the capture
sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

#at windows-like we must send an IOCTL to enable promiscuo mode
if os.name  ==  "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

try:

    #read a package
    raw_buffer  =   sinnfer.recvfrom(65565)[0]

    #create an ip header from the 20 first bytes of the buffer
    ip_header   =   IP(raw_buffer[0:20])

    #show the detected protocols
    print"[#] Protocol: %s %s - > %s"% (ip_header.protocol, ip_header.src_address, ip_header.dst_address)

except KeyboardInterrupt:

    #if we're i windows-like, disable the promiscuos mode
    if os.name  ==  "nt":
        sniffer.ioctl(socket.SIO_RECVALL. socket.RECVALL_OFF)


