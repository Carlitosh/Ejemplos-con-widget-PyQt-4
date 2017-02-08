#!/usr/bin/python
# -*- coding: utf-8 -*-

#=======================================================================
#=======================Corregido - En funcionamiento ==================
#=======================================================================


import sys
from PyQt4 import QtGui, uic
from juliano_gregoriano import * 

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("maquetado.ui")[0]

class ventana_ejemplo(QtGui.QMainWindow, form_class):
	
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.cal.setGridVisible(True)
		
		self.boton_ejecutar.clicked.connect(self.ejecutar)
		
        
		
		
	def ejecutar(self):
		a =   self.cal.selectedDate()
		self.label.setText(a.toString())
		self.lineEdit.setText(a.toString())
		
		b = self.date.date()
		print b , a 
		self.label_2.setText(b.toString())
		
		

		


app = QtGui.QApplication(sys.argv)
ejemplo = ventana_ejemplo(None)
ejemplo.show()
app.exec_()


