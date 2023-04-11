import socket as sock

serverPort = 12000
serverSocket = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

