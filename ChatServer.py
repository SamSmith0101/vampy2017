import socket

phone = socket.socket()
addr = (socket.gethostname(),1738)
phone.bind(addr)
phone.listen(17)
while True:
	try:
		conn,cid = phone.accept()
		msg = bytes.decode(conn.recv(1024))
		conn.send("r".encode("UTF-8"))
		conn.close()
		print("Call from {0}: {1}.".format(cid,msg))
	except KeyboardInterrupt:
		phone.close()
		break
	except:
		print("Something unexpected happend, shutting down")
		phone.shutdown()
		break
