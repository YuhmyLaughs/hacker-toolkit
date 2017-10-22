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

#reads a single package
print sniffer.recvfrom(65565)

#if we're i windows-like, disable the promiscuos mode
if os.name  ==  "nt":
    sniffer.ioctl(socket.SIO_RECVALL. socket.RECVALL_OFF)


