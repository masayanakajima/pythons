from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Draw(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.initUI()

	def initUI(self):
		self.pixmap=QPixmap(QSize(400,400))
		self.resize(400,400)
		label=QLabel(self)
		label.setPixmap(self.pixmap)
		self.show()

	def paintEvent(self,e):
		painter = QPainter(self.pixmap)
		painter.begin(self)
		self.fillRect(QRectF(0,0,400,400),brush)

if __name__=="__main__":
	app=QApplication(sys.argv)
	draw=Draw()
	sys.exit(app.exec_())