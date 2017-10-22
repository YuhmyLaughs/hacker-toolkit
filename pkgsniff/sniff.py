import socket 
import os

#listenning host
host    =   raw_input(':: Type the listenning host IP ::')

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


