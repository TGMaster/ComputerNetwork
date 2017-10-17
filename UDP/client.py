import socket

array = ""
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 12000)

num = input ('Enter how many students: ')
print ('Enter student name: ')
for i in range(int(num)):
	temp = input('Name: ')
	array += temp + '\n'

message = array.encode()
clientSocket.sendto(message,server_address)
data, adr = clientSocket.recvfrom(1024)
message = data.decode()
print ('Received from server:\n' + message)

clientSocket.close()
