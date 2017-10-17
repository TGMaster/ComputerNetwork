import socket

array = "" #initialize string
server_address = ('127.0.0.1',12000) #set ip address and port number to connect to the server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #use TCP
clientSocket.connect(server_address) #connect to server

num = input ('Enter how many students: ')
print ('Enter student name: ')
for i in range(int(num)): #start loop to enter student name
	temp = input('Name: ')
	array += temp + '\n'

message = array.encode() #in python3 must encode to UTF-8
clientSocket.sendall(message) #send message to server
data = clientSocket.recv(2048) #receive message from server
message = data.decode() #decode it!
print ('Received from server:\n' + message) #print message

clientSocket.close() #close connection
