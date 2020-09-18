import socket

CAMIPADDR1 = '192.168.100.81'
PORTNUM = 1259

socketreceive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketreceive.bind(('127.0.0.1',PORTNUM))
while True:
	data, addr = socketreceive.recvfrom(1024)
	print("received message: %s" % data)
	#print("length: %s" % len(data))
	rawdatalen = len(data)
	#print (type(data))
	frame = b""
	frame += b'\x00' 
	frame += bytes.fromhex(format(rawdatalen+2, '02x'))
	frame += data
	print("sending message: %s" % frame)
	socketsend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
	socketsend.connect((CAMIPADDR1, PORTNUM))
	socketsend.send(frame)
	socketsend.close()