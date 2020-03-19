import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
	def __init__(self):
		super(Example,self).__init__()
		self.initUI()

	def initUI(self):
		exitAction = QtGui.QAction(QtGui.QIcon("test.jpg"),"&Exit",self)
		exitAction.setShortcut("Ctrl+Q")
		exitAction.setStatusTip("Exit application")
		exitAction.triggered.connect(QtGui.qApp.quit)
		self.statusBar()

		self.toolbar=self.addToolBar("Exit")
		self.toolbar.addAction(exitAction)

		menubar=self.menuBar()
		fileMenu=menubar.addMenu("&File")
		fileMenu.addAction(exitAction)

		self.statusBar().showMessage("Ready")
		self.setWindowTitle("Statusbar")
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())

if __name__=="__main__":
	main()