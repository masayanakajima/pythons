from socket import *
from PyQt4 import QtGui,QtCore
import sys


HOST="localhost"
PORT=21567
BUFSIZE=500000
ADDR=(HOST,PORT)
tcpSerSock=socket(AF_INET,SOCK_STREAM)


class Receiver(QtGui.QWidget):

	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.timer=QtCore.QBasicTimer()
		self.initUI()
		self.timer.start(30,self)

	def initUI(self):
		self.setWindowTitle("kasaya")
		self.label=QtGui.QLabel(self)
		self.label.resize(600,400)
		self.center()
		self.show()

	def center(self):
		screen=QtGui.QDesktopWidget().screenGeometry()
		self.resize(600,400)
		size=self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

	def timerEvent(self,event):
		data=tcpCliSock.recv(BUFSIZE)
		qPixmap=QtGui.QPixmap()
		qPixmap.loadFromData(data,"PNG")
		self.label.setPixmap(qPixmap)

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	tcpSerSock.bind(ADDR)
	tcpSerSock.listen(1)

	print("waiting for connection")
	tcpCliSock,addr = tcpSerSock.accept()
	receiver=Receiver()
	sys.exit(app.exec_())
