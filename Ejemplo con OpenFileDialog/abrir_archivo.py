#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, uic
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("maquetado.ui")[0]

class ventana_ejemplo(QtGui.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
		self.abrir_button.clicked.connect(self.abrir)
		
	def abrir(self):
		fname = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Capa vectorial', 
		'/home','(*.shp)')
		
		#obser = unicode(self.lineEdit.toPlainText())

		#obser1 = obser.encode('utf-8')
		unicode(self.lineEdit.setText(str(fname))).encode('utf-8')
		

app = QtGui.QApplication(sys.argv)
ejemplo = ventana_ejemplo(None)
ejemplo.show()
app.exec_()			
	









