#!/usr/bin/python2
import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1],int(sys.argv[2])))
answer = s.recv(1024)
print(answer)

s.send("USER anonymous\r\n")
answer = s.recv(1024)
print(answer)

s.send("PASS anonymous\r\n")
answer = s.recv(1024)
print(answer)

s.send("PWD \r\n")
#s.send("WHOAMI \r\n")
s.send("QUIT \r\n")
