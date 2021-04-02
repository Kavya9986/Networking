from socket import *
serverName="192.168.43.12"
serverPort=12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print( "You are online !")

while True:
    message = raw_input("Me:")
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(1028)
    print("She: " + modifiedMessage.decode())
    if message=="bye":    
        clientSocket.close()
        exit()