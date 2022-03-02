#*__*- UTF-8 -*__*
	#by: MiDo 
	#FB.com/mido.de3vil
from win10toast import ToastNotifier
import time
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QStyleOptionComboBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from sys import argv
from sys import exit 
from os import path
from datetime import datetime
from pdf2docx import parse
from PyQt5 import QtCore
from time import sleep
import webbrowser
from proj import Ui_MainWindow as DS

class Thread(QThread):
	time = pyqtSignal(str)
	conv = pyqtSignal(str)
	def run(self):
		while True:
			time = datetime.now()
			output = f'{time.hour}-{time.minute}-{time.second}'
			self.time.emit(output)
			QThread.msleep(1)		
class Thread_file(QThread):
	def __init__(self , main):
		super().__init__()
		self.main = main
	def mido(self):
		toaster = ToastNotifier()
		toaster.show_toast("Converter",
		                   "fileconverter finish",
		                   icon_path=r"E:\Coureses\python_Desktopapp_projects_exe\conv_exe\\ppdf.ico",
		                   duration=8,
		                   threaded=True)
		while toaster.notification_active(): time.sleep(0.1)
	def run(self):
		try:
			done = self.main.label_3
			pdf_name = self.main.lineEdit.text()
			docx = pdf_name+'.docx'
			conv = parse(pdf_name, docx , start=0, end=None)



		except Exception:
			pass
		done.setText('Done')
		self.mido()
		QThread.sleep(2)
		done.clear()
		done.setStyleSheet('None')
		

class FMainApp (QMainWindow ,DS ):
	def __init__(self , parent=None):
		super(FMainApp,self).__init__(parent)
		self.setupUi(self)
		self.setGeometry(730,330,500,400)
		self.remove_titrl_bar()
		self.thread = Thread()
		self.thread2 = Thread_file(self)
		self.thread.time.connect(self.set_time)
		self.thread.start()
		self.buttn()
		self.doShake()




	def doShake(self):
		self.doShakeWindow(self)
	def doShakeWindow(self, target):
		if hasattr(target, '_shake_animation'):
			return

		animation = QPropertyAnimation(target, b'pos', target)
		target._shake_animation = animation
		animation.finished.connect(lambda: delattr(target, '_shake_animation'))
		pos = target.pos()
		x, y = pos.x(), pos.y()
		animation.setDuration(150)
		animation.setLoopCount(3.5)
		animation.setKeyValueAt(0, QPoint(x, y))
		animation.setKeyValueAt(1.09, QPoint(x + 5, y - 2))
		animation.setKeyValueAt(0.18, QPoint(x + 4, y - 4))
		animation.setKeyValueAt(0.27, QPoint(x + 2, y - 6))
		animation.setKeyValueAt(0.36, QPoint(x + 0, y - 8))
		animation.setKeyValueAt(0.45, QPoint(x - 2, y - 10))
		animation.setKeyValueAt(0.54, QPoint(x - 4, y - 8))
		animation.setKeyValueAt(0.63, QPoint(x - 6, y - 6))
		animation.setKeyValueAt(0.72, QPoint(x - 8, y - 4))
		animation.setKeyValueAt(0.81, QPoint(x - 6, y - 2))
		animation.setKeyValueAt(0.90, QPoint(x - 4, y - 0))
		animation.setKeyValueAt(0.99, QPoint(x - 2, y + 2))
		animation.setEndValue(QPoint(x, y))
		animation.start(animation.DeleteWhenStopped)

	def mousePressEvent(self, e):
		self.previous_pos = e.globalPos()

	def mouseMoveEvent(self, e):
		delta = e.globalPos() - self.previous_pos
		self.move(self.x() + delta.x(), self.y()+delta.y())
		self.previous_pos = e.globalPos()
		self._drag_active = True
###########################################################################
##################################################################
	def remove_titrl_bar(self):
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	def set_time(self , value):
			self.label.setText(value)
	def browse(self):
		save =  QFileDialog.getOpenFileName(self,"Select pdf file",filter='*.pdf')
		path_name = save[-2]
		p = ''
		p += path_name
		name = p.split('/')[-1]
		nams = str(name)
		mido = self.lineEdit.setText(str(p))
	def buttn(self):
		self.pushButton.clicked.connect(self.browse)
		self.pushButton_2.clicked.connect(self.convetr)
		self.pushButton_3.clicked.connect(lambda: self.close())
		self.pushButton_4.clicked.connect(self.m)
		self.pushButton_5.clicked.connect(self.fac)

	def ext(self):
		exit()
	def convetr(self):
		pdf_name = self.lineEdit.text()
		self.thread2 = Thread_file(self)
		self.thread2.start()
		sleep(0.5)
		self.lineEdit.clear()
		QThread.msleep(10)
		self.lodeng()
	def lodeng(self):
		self.label_3.setStyleSheet('background-color: rgb(0, 255, 0); border-radius:  10px; color: rgb(255, 0, 255); font: 9pt "MV Boli"; margin-left: 10px; margin-right: 10px;')
		
		self.label_3.setText('Lodeng..')


	def m(self):
		self.showMinimized()
	def fac(self):
		webbrowser.open("https://FB.com/De3vil.3")

def main():
	app = QApplication(argv)
	window = FMainApp()
	menu = QMenu()
	v = QSystemTrayIcon(QIcon(r"E:\Coureses\python_Desktopapp_projects_exe\conv_exe\\ppdf.ico"),app)
	v.setToolTip("Converter")
	menu = QMenu()
	action_exit = QAction("Exit")
	action_exit.triggered.connect(app.exit)
	menu.addAction(action_exit)

	action_show = QAction("Show Window")
	action_show.triggered.connect(window.show)
	menu.addAction(action_show)
	v.setContextMenu(menu)
	v.show()
	app.setQuitOnLastWindowClosed(False)
	window.show()
	app.exec_()

main()
