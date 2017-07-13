import socket

while True:
	n = input("Who do you want to call?")
	msg = input("What do you want to send?")
	data = msg.encode("UTF-8")
	phone = socket.socket()
	addr = ("vampy-cs-"+n,8080)
	phone.connect(addr)
	phone.send(data)
	resp = bytes.decode(phone.recv(1024))
	if resp != "r":
		print("Ooops, something was done wrong.")
	phone.close()

