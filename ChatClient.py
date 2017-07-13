import socket

group = ["5", "9", "13"]
while True:
	msg = input("What do you want to send?")
	data = msg.encode("UTF-8")
	try:
		for i in group:
			phone = socket.socket()
			addr = ("vampy-cs-"+i,1738)
			phone.connect(addr)
			phone.send(data)
			resp = bytes.decode(phone.recv(1024))
			if resp != "r":
				print("Ooops, something was done wrong.")
			phone.close()
	except KeyboardInterrupt:
		phone.close()
		break		
