from socket import *

f=open("ip.txt")
HOST=f.read()
PORT=21567
ADDR=(HOST,PORT)
BUFSIZE=10240

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data=raw_input(">")
	
	tcpCliSock.send(data)
	data=tcpCliSock.recv(BUFSIZE)
	print data
	