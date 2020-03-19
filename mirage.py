# -*- coding: utf-8 -*-
from PyQt4 import QtCore,QtGui
import sys

class KasayaPixmap(QtGui.QPixmap):
	def __init__(self,x,y,maxW,maxH):
		QtGui.QPixmap.__init__(self,"shade2.jpg")
		self.x=x
		self.y=y
		self.maxW=maxW
		self.maxH=maxH
		self.width=0
		self.height=0
		self.count=0

	def draw(self,painter):
		if self.count==0:
			return

		xoff=self.x*self.maxW+self.maxW/2-self.width/2
		yoff=self.y*self.maxH+self.maxH/2-self.height/2
		painter.drawPixmap(xoff,yoff,self.width,self.height,self)
		if xoff-self.x*self.maxW<=2 or yoff-self.y*self.maxH<=2:
			self.width=0
			self.height=0
			self.count+=1
			if self.count==30:
				self.count=0
		else:
			self.width+=self.maxW/10
			self.height+=self.maxH/10

	def countStart(self):
		self.count=1


class Mirage(QtGui.QWidget):

	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.height=0
		self.row=8
		self.col=10
		self.initUI()
		self.timer=QtCore.QBasicTimer()
		self.list=list()
		for i in range(0,self.row):
			for j in range(0,self.col):
				self.list.append(KasayaPixmap(j,i,self.w,self.h))
		
	def initUI(self):
		screen=QtGui.QDesktopWidget().screenGeometry()
		self.w=screen.width()/self.col
		self.h=screen.height()/self.row
		self.showFullScreen()
		self.desktop=QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId())
		self.kasaya=QtGui.QPixmap("shade2.jpg")
		self.alphachannel=QtGui.QPixmap(screen.width(),screen.height())

	def paintEvent(self,e):
		qp1=QtGui.QPainter(self)
		qp2=QtGui.QPainter(self.alphachannel)

		color=QtGui.QColor(255-self.height,255-self.height,255-self.height)
		qp2.fillRect(0,0,self.desktop.width(),self.desktop.height(),color)
		
		self.desktop.setAlphaChannel(self.alphachannel)
		qp2.end()
		for i in range(0,self.row):
			for j in range(0,self.col):
				qp1.drawPixmap(j*self.w,i*self.h,self.w,self.h,self.kasaya)
		
		for kasaya in self.list:
			kasaya.draw(qp1)

		qp1.drawPixmap(0,0,self.desktop)
		qp1.end()

	def timerEvent(self,e):
		self.repaint()

	def mousePressEvent(self,e):
		if self.height<25:
			self.height+=1
			self.repaint()
			QtGui.QSound.play("stop.wav")
		else:
			QtGui.QSound.play("kimowarai.wav")
			for kasaya in self.list:
				kasaya.countStart()
			self.timer.start(10,self)

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	mirage=Mirage()
	sys.exit(app.exec_())
