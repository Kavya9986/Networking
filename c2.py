from socket import *
serverName="192.168.43.12"
serverPort=12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print( "You are online !")

while True:
    modifiedMessage = clientSocket.recv(1028)
    print("She: " + modifiedMessage.decode())
    message = raw_input("Me:")
    clientSocket.send(message.encode())        
    if message=="bye":    
        clientSocket.close()
        exit()
    
