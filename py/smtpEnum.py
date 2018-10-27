#!/usr/bin/python2
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1],25))
banner = s.recv(1024)
print banner

s.send('VRFY '+ sys.argv[2]'+\r\n')
answer = s.recv(1024)
print answer
