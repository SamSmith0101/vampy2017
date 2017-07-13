import socket
phone = socket.socket()
addr = (socket.gethostname,8080)
phone.bind(address)
phone.listen(17)
while True:
	try:
		conn,cid = phone.accept()
		msg = bytes.decode(conn.recv(1024))
		conn.send("r".encode("r"))
		conn.close()
		print("Call from {0}: {1}.".format(cid,msg))
	except KeyboardInterrupt:
		phone.close()
		break
