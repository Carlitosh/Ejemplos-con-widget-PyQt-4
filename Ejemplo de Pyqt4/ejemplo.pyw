#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, uic
import os
from pylab import *
 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("ejemplo.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.ayuda)
		self.pushButton_2.clicked.connect(self.abrir)
		self.pushButton_3.clicked.connect(self.graficar)
		self.acerca.triggered.connect(self.action)
  
	def action(self):
		os.system('pythonw acerca.pyw')
	
	def abrir(self):
		os.system('python calculadorafisica.py')
		
	def graficar(self):


		t = arange(0.0, 2.0, 0.01)
		form =  int(self.lineEdit1.text())
		s = sin(form)
		plot(t, s)

		xlabel('time (s)')
		ylabel('voltage (mV)')
		title('About as simple as it gets, folks')
		grid(True)
		#savefig("test.png")
		show()
		
	
	def ayuda(self):

		a = int(self.lineEdit1.text())
		b = int(self.lineEdit2.text())
		c = int(self.lineEdit3.text())

		d = (-b - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
		e = (-b + ((b ** 2 - 4 * a * c)** 0.5)) / (2 * a)	

		self.textEdit1.setText(str(d))
		self.lineEdit_1.setText(str(d))
		self.textEdit2.setText(str(e))
		self.lineEdit_2.setText(str(d))


app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
