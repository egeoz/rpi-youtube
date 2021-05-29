#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Youtube player --- Server

import socket, os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("1.1.1.1", 1))
localIP = s.getsockname()[0]
localPort   = 20001
bufferSize  = 1024

msg = "Connection established with the server at: {}".format(localIP)
b = str.encode(msg)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP,localPort))

print("Server is up and listening...")

while(True):
    recv = UDPServerSocket.recvfrom(bufferSize)
    link = recv[0]
    address = recv[1]
    clientIP  = "Client IP Address:{}".format(address)
    print(address," sent link ", link)
    os.system("vlc " + str(link)[1:] + " &")
    UDPServerSocket.sendto(str.encode("Link received."), address)
