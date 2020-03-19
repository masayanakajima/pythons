from socket import *
from PyQt4 import QtGui,QtCore
import sys

HOST="localhost"
PORT=21567
ADDR=(HOST,PORT)
BUFSIZE=500000

tcpCliSock=socket(AF_INET,SOCK_STREAM)

class Sender(QtGui.QWidget):

	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.timer=QtCore.QBasicTimer()
		self.timer.start(30,self)

	def timerEvent(self,event):
		pixmapQt=QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId()).scaled(600,400)
		buffer=QtCore.QBuffer()
		buffer.open(QtCore.QIODevice.WriteOnly)
		pixmapQt.save(buffer,"PNG")
		data=buffer.data()
		tcpCliSock.send(data)

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	tcpCliSock.connect(ADDR)
	sender=Sender()
	sys.exit(app.exec_())
