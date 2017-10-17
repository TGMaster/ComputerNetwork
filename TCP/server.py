import socket
 
server_address = ('127.0.0.1',12000) #set ip address and port number for server
    
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #use TCP
serverSocket.bind(server_address) #assign port number to socket
     
serverSocket.listen(1) #The server listen for TCP connection requests from the client.
print ("The server is ready to receive")
conn, addr = serverSocket.accept()
print ("Connection from: " + str(addr))
while True:
	data = conn.recv(2048)
	data = data.decode()
	if not data: #if no data receive, break the loop
		break
	print ('Uppercase processing...')
	data = str(data).upper()
	print ('Sending back to client...')
	conn.sendall(data.encode())
	print ('Printing text file...')
	text = open("Output.txt", "w")
	text.write(data)
	text.close()

conn.close()
