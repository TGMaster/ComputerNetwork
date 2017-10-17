import socket

array = ""
server_address = ('127.0.0.1',12000)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(server_address)

num = input ('Enter how many students: ')
print ('Enter student name: ')
for i in range(int(num)):
	temp = input('Name: ')
	array += temp + '\n'

message = array.encode()
clientSocket.sendall(message)
data = clientSocket.recv(2048)
message = data.decode()
print ('Received from server:\n' + message)

clientSocket.close()
