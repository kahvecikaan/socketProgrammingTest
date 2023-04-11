import socket as sock

serverName = "127.0.0.1"
serverPort = 12000
clientSocket = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
message = input("Input lowercase sentence: ")
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

clientSocket.close()
