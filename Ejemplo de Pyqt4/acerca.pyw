#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, uic
import os

 
# Cargar nuestro archivo .ui
form_class1 = uic.loadUiType("acerca.ui")[0]

class MyWindowClass1(QtGui.QMainWindow, form_class1):
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		
  
	


app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass1(None)
MyWindow.show()
app.exec_()

