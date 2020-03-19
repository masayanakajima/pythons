# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui,QtCore
from os.path import join,relpath
from glob import glob
from niconama import CommunityAnalyzer

class Gui(QtGui.QWidget):

	def __init__(self):
		super(Gui,self).__init__()
		self.analyzer=CommunityAnalyzer()
		self.initUI()
		self.setGeometry(800,400,450,350)
		self.setWindowTitle(u"ニコニコアナライザー")
		self.setWindowIcon(QtGui.QIcon("Shade.png"))
		self.show()
		

	def initUI(self):
		vbox=QtGui.QVBoxLayout()
		vbox.addLayout(self.addCommunityLayout())	
		self.analyzeLayout=self.analyzeLayout()
		vbox.addLayout(self.analyzeLayout)
		self.setLayout(vbox)
	
	def addCommunityLayout(self):
		vbox=QtGui.QVBoxLayout()

		self.urlEditor=QtGui.QLineEdit(self)
		self.txtEditor=QtGui.QLineEdit(self)

		vbox.addLayout(self.editorLayout(u"コミュニティメンバーのURL：",self.urlEditor))
		vbox.addLayout(self.editorLayout(u"ニックネーム：",self.txtEditor))

		hbox=QtGui.QHBoxLayout()
		self.addButton=QtGui.QPushButton(u"追加")
		self.addButton.clicked.connect(self.addCommunity)
		hbox.addWidget(self.addButton)
		hbox.addWidget(self.analyzer.addBar)

		vbox.addLayout(hbox)
		return vbox

	def editorLayout(self,detail,line_editor):
		hbox=QtGui.QHBoxLayout()
		label=QtGui.QLabel(detail)
		hbox.addWidget(label)
		hbox.addWidget(line_editor)
		return hbox

	def checkBoxArea(self):
		base = QtGui.QWidget()
		layout=QtGui.QVBoxLayout()
		base.setLayout(layout)

		path="namelist"
		files=[relpath(x,path) for x in glob(join(path,"*"))]
		self.checkboxList=[]
		for filename in files:
			self.checkboxList.append(QtGui.QCheckBox(filename))
		for checkbox in self.checkboxList:
			layout.addWidget(checkbox)

		return base

	def analyzeLayout(self):
		hbox=QtGui.QHBoxLayout()
		self.selection=self.selectionLayout()
		hbox.addLayout(self.selection)
		hbox.addLayout(self.resultLayout())

		return hbox

	def selectionLayout(self):
		vbox=QtGui.QVBoxLayout()
		self.scrollWidget=self.scrollArea()
		vbox.addWidget(self.scrollWidget)
		resetButton=QtGui.QPushButton(u"リセット")
		resetButton.clicked.connect(self.reset)
		vbox.addWidget(resetButton)
		return vbox

	def scrollArea(self):
		scrollWidget=QtGui.QScrollArea(self)
		scrollWidget.setWidget(self.checkBoxArea())
		return scrollWidget

	def resultLayout(self):
		vbox=QtGui.QVBoxLayout()
		vbox.addLayout(self.commonResultLayout())
		vbox.addLayout(self.searchResultLayout())
		return vbox

	def commonResultLayout(self):
		vbox=QtGui.QVBoxLayout()
		startButton=QtGui.QPushButton(u"分析開始")
		startButton.clicked.connect(self.analyze)
		vbox.addWidget(startButton)
		vbox.addWidget(self.analyzer.analyzeBar)
		self.result=QtGui.QLabel(u"共通のメンバーは"+"      "+u"人")
		vbox.addWidget(self.result)
		return vbox

	def searchResultLayout(self):
		vbox=QtGui.QVBoxLayout()
		self.userEditor=QtGui.QLineEdit()
		vbox.addLayout(self.editorLayout(u"ユーザー名：",self.userEditor))
		searchButton=QtGui.QPushButton(u"探索開始")
		searchButton.clicked.connect(self.search)
		vbox.addWidget(searchButton)
		self.searchresult=QtGui.QLabel()
		vbox.addWidget(self.searchresult)
		return vbox

	def addCommunity(self):
		self.analyzer.add_community(str(self.urlEditor.text()),str(self.txtEditor.text()))
		self.selection.removeWidget(self.scrollWidget)
		self.scrollWidget=self.scrollArea()
		self.selection.insertWidget(0,self.scrollWidget)

	def analyze(self):
		namelist=[]
		for checkbox in self.checkboxList:
			if(checkbox.isChecked()):
				namelist.append(str(checkbox.text()))
		self.result.setText(u"共通のメンバーは"+"  "+str(len(self.analyzer.get_intersection(namelist)))+"   "+u"人")	

	def search(self):
		username=self.userEditor.text().toUtf8().data().decode("utf-8")+str("\n")
		namelist=[]
		for checkbox in self.checkboxList:
			if(checkbox.isChecked()):
				namelist.append(str(checkbox.text()))
		commonlist=self.analyzer.get_intersection(namelist)
		self.searchresult.setText(str(len(self.analyzer.get_commons([username],commonlist))))

	def reset(self):
		for checkbox in self.checkboxList:
			if(checkbox.isChecked()):
				checkbox.toggle()

def main():
	app = QtGui.QApplication(sys.argv)
	gui = Gui()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()