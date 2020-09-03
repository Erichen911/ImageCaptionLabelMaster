import json
import os
import cv2
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import mainwindow
import sys
from PyQt5 import QtCore,QtWidgets,QtGui




class Window(QtWidgets.QMainWindow):
	# init
	def __init__(self,win):
		super().__init__()
		self.win = win
		self.initUI()

	# setvalue
	def initUI(self):
		self.setWindowTitle('Label')
		self.show()

	# keyPress
	def keyPressEvent(self, event):
		if (event.key() == Qt.Key_A):
			MainWindow.saveCSVPATH(self.win)
			self.win.index = self.win.index - 1
			if self.win.index < 0:
				self.win.index = 0
			MainWindow.setTheWindow(self.win)
			# MainWindow.make_listView(self.win)

		if (event.key() == Qt.Key_D):
			MainWindow.saveCSVPATH(self.win)
			self.win.index = self.win.index + 1
			if self.win.index >= len(self.win.image_list):
				self.win.index = len(self.win.image_list)-1
			MainWindow.setTheWindow(self.win)
			# MainWindow.make_listView(self.win)

		if (event.key() == Qt.Key_W):
			MainWindow.saveCSVPATH(self.win)
	# mouseEvent
	def mousePressEvent(self, event):
		pass


class MainWindow(object):
	def __init__(self):
		self.lv = []
		app = QtWidgets.QApplication(sys.argv)
		self.ui = mainwindow.Ui_MainWindow()
		self.index = 0

		windows = Window(self)
		self.ui.setupUi(windows)
		#self.load_json()
		#self.setTheWindow()

		self.ui.pushButton.clicked.connect(self.jump_plot)
		self.ui.AddButton_1.clicked.connect(self.addtxt1)
		self.ui.AddButton_2.clicked.connect(self.addtxt2)
		self.ui.AddButton_3.clicked.connect(self.addtxt3)
		self.ui.AddButton_4.clicked.connect(self.addtxt4)
		self.ui.AddButton_5.clicked.connect(self.addtxt5)
		self.ui.pushButton_2.clicked.connect(self.read_dic)
		self.ui.S1_1.currentIndexChanged.connect(self.sentence1_1)
		self.ui.S1_2.currentIndexChanged.connect(self.sentence1_2)
		self.ui.S2_1.currentIndexChanged.connect(self.sentence2_1)
		self.ui.S2_2.currentIndexChanged.connect(self.sentence2_2)
		self.ui.S3_1.currentIndexChanged.connect(self.sentence3_1)
		self.ui.S3_2.currentIndexChanged.connect(self.sentence3_2)
		self.init_lineedit()
		sys.exit(app.exec())

		# f = open("./style.qss", "r", encoding='utf-8')
		# windows.setStyleSheet(f.read())
		# f.close()



	def load_json(self):
		with open("config.json", "rb") as f:
			data = json.load(f)
		#self.image_path = data["image_path"]

		#self.image_list.sort(key=lambda x: int(x[self.before:]))

		#self.make_listView()

	def make_listView(self):
		self.lv = []
		save_data = np.array(pd.read_csv(self.save_path, index_col=0))
		for ind, im in enumerate(save_data):
			count = 0
			for sen in  im:
				if not type(sen) == float and not type(sen) == np.float64:
					count = count + 1
			self.lv.append(self.image_list[ind] + "     " + str(count))
		self.slm = QStringListModel()
		self.slm.setStringList(self.lv)
		self.ui.listlistview.setModel(self.slm)
		self.ui.listlistview.clicked.connect(self.clickedlist)


	def setTheWindow(self):
		image = self.image_list[self.index]
		print(image)
		jpg = QtGui.QPixmap(os.path.join(self.image_path, image))
		self.ui.ImageLabel.setPixmap(jpg)
		self.ui.ImageLabel.setScaledContents(True)
		save_data = pd.read_csv(self.save_path)
		self.ui.ImageName.setText(image)
		self.ui.NumName.setText(str(self.index))

		try:
			label = np.array(save_data[save_data["Unnamed: 0"] == self.image_list[self.index]])[0]
			self.ui.lineEdit.setText(str(label[1]))
			self.ui.lineEdit2.setText(str(label[2]))
			self.ui.lineEdit3.setText(str(label[3]))
			self.ui.lineEdit4.setText(str(label[4]))
			self.ui.lineEdit5.setText(str(label[5]))
		except:
			pass


	def saveCSVPATH(self):
		save_data = pd.read_csv(self.save_path, index_col=0)
		image = self.image_list[self.index]
		save_data.loc[image, "sentence1"] = self.ui.lineEdit.text()
		save_data.loc[image, "sentence2"] = self.ui.lineEdit2.text()
		save_data.loc[image, "sentence3"] = self.ui.lineEdit3.text()
		save_data.loc[image, "sentence4"] = self.ui.lineEdit4.text()
		save_data.loc[image, "sentence5"] = self.ui.lineEdit5.text()
		save_data.to_csv(self.save_path)
		data = np.array(save_data.loc[image])
		count = 0
		for d in data:
			if not d == "nan":
				count = count + 1
		self.lv[self.index] = self.lv[self.index][:-1] + str(count)
		self.slm.setStringList(self.lv)

	def jump_plot(self):
		image = self.ui.lineEdit_2.text()
		if image in self.image_list:
			index = self.image_list.index(image)
			self.saveCSVPATH()
			self.index = index
			self.setTheWindow()
		else:
			pass

	def addtxt1(self):
		with open("suggestlist.txt", "a+") as f:
			f.write(self.ui.lineEdit.text()+"\n")
		self.init_lineedit()
	def addtxt2(self):
		with open("suggestlist.txt", "a+") as f:
			f.write(self.ui.lineEdit2.text()+"\n")
		self.init_lineedit()
	def addtxt3(self):
		with open("suggestlist.txt", "a+") as f:
			f.write(self.ui.lineEdit3.text()+"\n")
		self.init_lineedit()
	def addtxt4(self):
		with open("suggestlist.txt", "a+") as f:
			f.write(self.ui.lineEdit4.text()+"\n")
		self.init_lineedit()
	def addtxt5(self):
		with open("suggestlist.txt", "a+") as f:
			f.write(self.ui.lineEdit5.text()+"\n")
		self.init_lineedit()

	def init_lineedit(self):
		#
		self.item_list = ["green"]
		with open("suggestlist.txt") as f:
			for line in f.readlines():
				self.item_list.append(line.strip())
		self.completer = QCompleter(self.item_list)
		# Qt.MatchStartsWith   Qt.MatchContains   Qt.MatchEndsWith
		self.completer.setFilterMode(Qt.MatchContains)
		# QCompleter.PopupCompletion  QCompleter.InlineCompletion   QCompleter.UnfilteredPopupCompletion
		self.completer.setCompletionMode(QCompleter.PopupCompletion)
		#
		self.ui.lineEdit.setCompleter(self.completer)
		self.ui.lineEdit2.setCompleter(self.completer)
		self.ui.lineEdit3.setCompleter(self.completer)
		self.ui.lineEdit4.setCompleter(self.completer)
		self.ui.lineEdit5.setCompleter(self.completer)

	def clickedlist(self, qModelIndex):
		self.saveCSVPATH()
		self.index = int(qModelIndex.row())
		self.setTheWindow()
		#self.make_listView()

	def read_dic(self):
		dic_name = QFileDialog.getExistingDirectory()
		self.image_path  = dic_name
		self.image_list = os.listdir(self.image_path)
		self.save_path = self.image_path+".csv"
		# self.image_list = os.listdir(self.image_path)
		if not os.path.exists(self.save_path):
			image_num = len(self.image_list)
			valid_sentence = np.full([image_num], np.nan)
			save_data = pd.DataFrame(
				{"sentence1": valid_sentence, "sentence2": valid_sentence, "sentence3": valid_sentence,
				 "sentence4": valid_sentence, "sentence5": valid_sentence})
			save_data.index = self.image_list
			save_data.to_csv(self.save_path)
		else:
			data = pd.read_csv(self.save_path)
			self.image_list = list(data['Unnamed: 0'])


		self.setTheWindow()

		self.make_listView()

	def sentence1_1(self):
		sen = "a " + self.ui.S1_1.currentText() + " bridge is on a " + self.ui.S1_2.currentText() + " river"
		self.ui.lineEdit.setText(sen)
	def sentence1_2(self):
		sen = "a " + self.ui.S1_1.currentText() + " bridge is on a " + self.ui.S1_2.currentText() + " river"
		self.ui.lineEdit.setText(sen)
	def sentence2_1(self):
		sen = "the " + self.ui.S2_1.currentText() + " of the bridge " + self.ui.S2_2.currentText()
		self.ui.lineEdit2.setText(sen)
	def sentence2_2(self):
		sen = "the " + self.ui.S2_1.currentText() + " of the bridge " + self.ui.S2_2.currentText()
		self.ui.lineEdit2.setText(sen)
	def sentence3_1(self):
		sen = self.ui.S3_2.currentText() + " on the " + self.ui.S3_1.currentText() + " part of the bridge"
		self.ui.lineEdit3.setText(sen)
	def sentence3_2(self):
		sen = self.ui.S3_2.currentText() + " on the " + self.ui.S3_1.currentText() + " part of the bridge"
		self.ui.lineEdit3.setText(sen)
if __name__ == '__main__':
	MainWindow()
# saveCSVPATH(ui, image_path, save_path, image_list)

	# app = QApplication(sys.argv)
	# ui = mainwindow.Ui_MainWindow()
	# window = Window()
	# ui.setupUi(window)
	# image_path, save_path, image_list = load_json()
	# setTheWindow(ui, image_path, save_path, image_list,0)
	# sys.exit(app.exec_())
