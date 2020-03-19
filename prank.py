# -*- coding: utf-8 -*-
from PyQt4 import QtCore,QtGui
import sys

class Prank(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self,parent=QtGui.QDesktopWidget())
		self.initUI()
		self.timer=QtCore.QBasicTimer()
		self.timer.start(1,self)

	def initUI(self):
		self.setWindowTitle(u"いたずら")
		img=QtGui.QPixmap("shade.jpg")

		screen=QtGui.QDesktopWidget().screenGeometry()
		img=img.scaled(screen.width(),screen.height())
		
		label=QtGui.QLabel(self)
		label.setPixmap(img)

		icon=QtGui.QIcon(img)
		self.setWindowIcon(icon)
		
		self.center()
		self.setWindowState(QtCore.Qt.WindowActive)
		self.show()

	def center(self):
		#self.resize(400,600)
		#screen=QtGui.QDesktopWidget().screenGeometry()
		#size=self.geometry()
		#self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
		self.showFullScreen()
	
	def hideEvent(self,event):
		self.center()
		print("hide")

	def resizeEvent(self,event):
		self.center()
		print("resize")

	def moveEvent(self,event):
		self.center()

	def timerEvent(self,event):
		self.activateWindow()
		self.raise_()

	def keyReleaseEvent(self,event):
		print "Release"
		self.center()

def main():
	app=QtGui.QApplication(sys.argv)
	gui=Prank()
	sys.exit(app.exec_())

if __name__=="__main__":
	main()