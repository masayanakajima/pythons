# -*- coding: utf-8 -*-
import sys
import BroadcastObserver
from PyQt4 import QtGui,QtCore

class Gui(QtGui.QWidget):
	def __init__(self):
		super(Gui,self).__init__()
		self.observer=BroadcastObserver.BroadcastObserver(self)
		self.initUI()


	def initUI(self):
		grid=QtGui.QGridLayout()
		self.urllabel=QtGui.QLabel(u"放送ページのURL")
		self.urledit=QtGui.QLineEdit(self)
		self.urledit.returnPressed.connect(self.sendurl)
		
		grid.addWidget(self.urllabel,0,0)
		grid.addWidget(self.urledit,1,0)

		self.setLayout(grid)

		self.resize(400,150)
		self.center()
		self.setWindowTitle("Next")
		self.show()

	def center(self):
		screen=QtGui.QDesktopWidget().screenGeometry()
		size=self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

	def sendurl(self):
		self.observer.receiveurl(str(self.urledit.text()))

def main():
	app=QtGui.QApplication(sys.argv)
	gui=Gui()
	sys.exit(app.exec_())

if __name__=="__main__":
	main()