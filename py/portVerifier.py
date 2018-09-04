#!/usr/bin/python

import socket

ip = raw_input("Type your ip :: ")
port = int(raw_input("Type the port number :: "))

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if mysocket.connect_ex((ip, port)):
	print("Oh.. it's open folks..")
else:
	print(":( It's closed..")


