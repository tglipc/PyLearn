#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import sys

if len(sys.argv) > 1:
    host = sys.argv[1]
else:
    host = input('Connect to: ')

while True:
    command = input('Send command: ')
    if command is 'q':
        break
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, 20000))
    sock.send(bytes(command, 'UTF-8'))
    ret = sock.recv(2048).decode('utf8')
    print(ret)
    sock.close()
