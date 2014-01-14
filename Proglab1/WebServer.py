'''
Created on 10. jan. 2014

@author: Robin
'''
#import socket module 

from socket import * 

serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a server socket 

#Fill in start
serverHost = 'localhost'
serverPort = 8000
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'

#Fill in end 

while True: 
    #Establish the connection 
    print 'Ready to serve...' 
    connectionSocket, addr = serverSocket.accept() 
    try: 
        message = connectionSocket.recv(1024)
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = f.read() 
        #Send one HTTP header line into socket 
        #Fill in start 
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
        #Fill in end 
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i]) 
        connectionSocket.close() 
    except IOError: 
        #Send response message for file not found 
        connectionSocket.send('404 Not Found')
        
        connectionSocket.close()
serverSocket.close() 
