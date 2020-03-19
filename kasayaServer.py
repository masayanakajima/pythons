from socket import *
import StringIO
from PyQt4 import QtGui,QtCore
import sys

HOST="192.168.11.2"
PORT=21567
BUFSIZE=500000
ADDR=(HOST,PORT)
tcpSerSock=socket(AF_INET,SOCK_STREAM)

class Receiver(QtGui.QWidget):

	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.timer=QtCore.QBasicTimer()
		self.initUI()
		self.timer.start(300,self)
		self.bufferPixmap=QtGui.QPixmap()
		
		
	def initUI(self):
		self.setWindowTitle("kasaya")
		self.center()
		self.show()

	def center(self):
		screen=QtGui.QDesktopWidget().screenGeometry()
		self.resize(1000,800)
		size=self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

	def timerEvent(self,event):
		self.repaint()

	def paintEvent(self,event):
		data=tcpCliSock.recv(BUFSIZE)
		painter=QtGui.QPainter(self)
		painter.drawPixmap(0,0,1000,800,self.bufferPixmap)
		self.bufferPixmap.loadFromData(data,"JPEG")
		#if self.bufferPixmap.loadFromData(data,"JPEG"):
		#	painter.drawPixmap(0,0,1000,800,self.bufferPixmap)

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	tcpSerSock.bind(ADDR)
	tcpSerSock.listen(1)

	print "waiting for connection"
	tcpCliSock,addr = tcpSerSock.accept()
	print "...connected from:",addr
	receiver=Receiver()
	sys.exit(app.exec_())
		