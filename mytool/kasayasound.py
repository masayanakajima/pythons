import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

class Example(QWidget):
	def __init__(self):
		super(Example,self).__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300,300,800,500)
		self.setWindowTitle("kasayasound")
		
		self.list=[]
	  
		self.sound = {"a":QSound("a.wav"),"i":QSound("i.wav"),"u":QSound("u.wav"),"e":QSound("e.wav"),"o":QSound("o.wav"),
					  "ka":QSound("ka.wav"),"ki":QSound("ki.wav"),"ku":QSound("ku.wav"),"ke":QSound("ke.wav"),"ko":QSound("ko.wav"),
					  "ga":QSound("ga.wav"),"gi":QSound("gi.wav"),"gu":QSound("gu.wav"),"ge":QSound("ge.wav"),"go":QSound("go.wav"),
					  "sa":QSound("sa.wav"),"si":QSound("si.wav"),"su":QSound("su.wav"),"se":QSound("se.wav"),"so":QSound("so.wav"),
					  "za":QSound("za.wav"),"zi":QSound("zi.wav"),"zu":QSound("zu.wav"),"ze":QSound("ze.wav"),"zo":QSound("zo.wav"),
					  "ta":QSound("ta.wav"),"ti":QSound("ti.wav"),"tu":QSound("tu.wav"),"te":QSound("te.wav"),"to":QSound("to.wav"),
					  "da":QSound("da.wav"),"ji":QSound("ji.wav"),"du":QSound("du.wav"),"de":QSound("de.wav"),"do":QSound("do.wav"),
					  "na":QSound("na.wav"),"ni":QSound("ni.wav"),"nu":QSound("nu.wav"),"ne":QSound("ne.wav"),"no":QSound("no.wav"),
					  "ha":QSound("ha.wav"),"hi":QSound("hi.wav"),"hu":QSound("hu.wav"),"he":QSound("he.wav"),"ho":QSound("ho.wav"),
					  "ba":QSound("ba.wav"),"bi":QSound("bi.wav"),"bu":QSound("bu.wav"),"be":QSound("be.wav"),"bo":QSound("bo.wav"),
					  "pa":QSound("pa.wav"),"pi":QSound("pi.wav"),"pu":QSound("pu.wav"),"pe":QSound("pe.wav"),"po":QSound("po.wav"),
					  "ma":QSound("ma.wav"),"mi":QSound("mi.wav"),"mu":QSound("mu.wav"),"me":QSound("me.wav"),"mo":QSound("mo.wav"),
					  "ya":QSound("ya.wav"),"yu":QSound("yu.wav"),"yo":QSound("yo.wav"),
					  "ra":QSound("ra.wav"),"ri":QSound("ri.wav"),"ru":QSound("ru.wav"),"re":QSound("re.wav"),"ro":QSound("ro.wav"),
					  "wa":QSound("wa.wav"),"wo":QSound("wo.wav"),"nn":QSound("nn.wav")}

		self.key = {"a":Qt.Key_A,"b":Qt.Key_B,"c":Qt.Key_C,"d":Qt.Key_D,"e":Qt.Key_E,"f":Qt.Key_F,"g":Qt.Key_G,
					"h":Qt.Key_H,"i":Qt.Key_I,"j":Qt.Key_J,"k":Qt.Key_K,"l":Qt.Key_L,"m":Qt.Key_M,"n":Qt.Key_N,
					"o":Qt.Key_O,"p":Qt.Key_P,"q":Qt.Key_Q,"r":Qt.Key_R,"s":Qt.Key_S,"t":Qt.Key_T,"u":Qt.Key_U,
					"v":Qt.Key_V,"w":Qt.Key_W,"x":Qt.Key_X,"y":Qt.Key_Y,"z":Qt.Key_Z}

		self.show()

	def keyPressEvent(self,event):
		key = event.key()
		self.searchKey(key)
		self.makeSound()

	def searchKey(self,input_key):
		for key,value in self.key.items():
			if input_key==value:
				self.list.append(key)

	def makeSound(self):
		input_str="".join(self.list)
		print(input_str)
		if input_str in self.sound:#.has_key(input_str):
			self.sound[input_str].play()
			self.list=[]
		elif len(input_str) == 3:
			self.list=[]
	

if __name__ == "__main__":
	app = QApplication(sys.argv)

	ex=Example()

	sys.exit(app.exec_())
