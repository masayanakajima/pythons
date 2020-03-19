# -*- coding: utf-8 -*-
from PyQt4 import QtCore,QtGui
import sys

class Prank(QtGui.QWidget):
	width=800
	height=600
	interval=30
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.timer=QtCore.QBasicTimer()
		self.initUI()
		
	def initUI(self):
		self.setWindowTitle(u"いたずら")
		self.label=QtGui.QLabel(self)
		self.label.resize(Prank.width,Prank.height)
		self.center()	
		self.timer.start(Prank.interval,self)
		self.show()

	def center(self):

		screen=QtGui.QDesktopWidget().screenGeometry()
		self.resize(Prank.width,Prank.height)
		size=self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

	def timerEvent(self,event):
		pixmapQt=QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId()).scaled(Prank.width,Prank.height)
		self.label.setPixmap(pixmapQt)
		#self.timer.start(Prank.interval,self)

	def resizeEvent(self,event):
		Prank.width=event.size().width()
		Prank.height=event.size().height()
		self.label.resize(Prank.width,Prank.height)
		
def main():
	app=QtGui.QApplication(sys.argv)
	prank=Prank()
	sys.exit(app.exec_())

if __name__=="__main__":
	main()
