#!/usr/bin/python
import socket,sys

for p in range(1,65535):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex((sys.argv[1],p)) == 0:
		print("Port ",p,"[OPEN]")
		s.close()
