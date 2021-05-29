import socket, subprocess

link = subprocess.check_output("termux-clipboard-get")
#bytesToSend = str.encode(link)
serverAddressPort = ("192.168.1.28", 20001)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(link, serverAddressPort)
msg = UDPClientSocket.recvfrom(bufferSize)

print("Reply from server: " , msg)
