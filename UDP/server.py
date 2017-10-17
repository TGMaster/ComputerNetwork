import socket

server_address = ('127.0.0.1', 12000)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind(server_address)
print('The server is ready to receive')

while True:
	message, addr = serverSocket.recvfrom(1024)
	data = message.decode()
	if not data:
		break
	print ('Uppercase processing...')
	data = str(data).upper()
	print ('Sending back to client...')
	serverSocket.sendto(data.encode(), addr)
	print ('Printing text file...')
	text = open("Output.txt", "w")
	text.write(data)
	text.close()

serverSocket.close()
