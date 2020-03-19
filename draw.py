import sys
from PyQt4 import QtGui,QtCore

class Paint(QtGui.QWidget):

	def __init__(self):
		super(Paint,self).__init__()
		self.initUI()
		self.height=0
		self.timer=QtCore.QBasicTimer()	
		self.timer.start(100,self)

	def initUI(self):
		self.pixmap=QtGui.QPixmap("test.jpg")
		self.setWindowTitle("Paint")
		self.resize(self.pixmap.width(),self.pixmap.height())
		self.show()

	def paintEvent(self,e):
		qp=QtGui.QPainter(self)
		qp.drawPixmap(0,0,self.pixmap)
		color=QtGui.QColor(255,0,0,200)
		qp.fillRect(0,0,self.pixmap.width(),self.height,color)
		qp.end()

	def timerEvent(self,e):
		self.height+=2
		self.repaint()

def main():
	app=QtGui.QApplication(sys.argv)
	paint=Paint()
	sys.exit(app.exec_())

if __name__=="__main__":
	main()