from socket import *

serverPort_c1 = 12000
serverPort_c2 = 12001

serverSocket_c1 = socket(AF_INET, SOCK_STREAM)
serverSocket_c2 = socket(AF_INET, SOCK_STREAM)

serverSocket_c1.bind(("", serverPort_c1))
serverSocket_c2.bind(("", serverPort_c2))

serverSocket_c1.listen(1)
serverSocket_c2.listen(1)

print("The server is ready to receive")

connectionSocket1, addr1 = serverSocket_c1.accept() 
connectionSocket2, addr2 = serverSocket_c2.accept()

while True:
    message = connectionSocket1.recv(1024)
    connectionSocket2.send(message)
    message_new = connectionSocket2.recv(1024)
    connectionSocket1.send(message_new)
    