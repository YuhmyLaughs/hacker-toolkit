#!/usr/bin/python2
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.13',25))
banner = s.recv(1024)
print banner
