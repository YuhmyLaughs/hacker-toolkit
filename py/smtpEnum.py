#!/usr/bin/python2
import socket
import sys
if len(sys.argv) != 3:
    print "Usage: python smtpEnum.py <IP> <user_list.txt>"
    sys.exit(0)
user_file = open(argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1],25))
banner = s.recv(1024)
print banner
for user in user_file.readlines():
    s.send('VRFY '+ sys.argv[2]'+\r\n')
    answer = s.recv(1024)
    print answer
