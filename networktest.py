import socket

host = ''
port = 8081

s = socket.socket()

information = (host,port)

s.bind(information)

s.listen(8)

conn, addr = s.accept()

print("Connection accepted")
while True:
	data = conn.recv(1024)
	message = data[:-2].decode('utf-8'))
	if(message == "hello"):
		print("No thanks")
