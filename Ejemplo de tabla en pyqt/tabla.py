#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui, uic
import sys 

 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("tabla.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
	
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.boton_insertar.clicked.connect(self.insertar)
		self.boton_sumar.clicked.connect(self.pp_anual)
		self.boton_graficar.clicked.connect(self.graficar)
		

		self.tableWidget.setColumnWidth(0,70);
		self.tableWidget.setColumnWidth(1,70);
		self.tableWidget.setColumnWidth(2,70);
		self.tableWidget.setColumnWidth(3,70);
		self.tableWidget.setColumnWidth(4,70);
		self.tableWidget.setColumnWidth(5,70);
		self.tableWidget.setColumnWidth(6,70);
		self.tableWidget.setColumnWidth(7,70);
		self.tableWidget.setColumnWidth(8,70);
		self.tableWidget.setColumnWidth(9,70);
		self.tableWidget.setColumnWidth(10,70);
		self.tableWidget.setColumnWidth(11,70);
		 
		
	
	
	def insertar(self):
		valor = ""
		self.valor = self.tableWidget.item(1,1).text()
		
		self.lineEdit1.setText(str(self.valor))
		
		print valor
		
	def pp_anual(self):
		
		self.pp_ene = int(self.tableWidget.item(0,0).text())
		self.pp_feb = int(self.tableWidget.item(0,1).text())
		self.pp_mar = int(self.tableWidget.item(0,2).text())
		self.pp_abr = int(self.tableWidget.item(0,3).text())
		self.pp_may = int(self.tableWidget.item(0,4).text())
		self.pp_jun = int(self.tableWidget.item(0,5).text())
		self.pp_jul = int(self.tableWidget.item(0,6).text())
		self.pp_ago = int(self.tableWidget.item(0,7).text())
		self.pp_sep = int(self.tableWidget.item(0,8).text())
		self.pp_oct = int(self.tableWidget.item(0,9).text())
		self.pp_nov = int(self.tableWidget.item(0,10).text())
		self.pp_dic = int(self.tableWidget.item(0,11).text())
		
		self.pp_anual = self.pp_ene + self.pp_feb + self.pp_mar + self.pp_abr + self.pp_may + self.pp_jun + self.pp_jul + self.pp_ago + self.pp_sep + self.pp_oct + self.pp_nov + self.pp_dic  
	
		self.lineEdit2.setText(str(self.pp_anual))
	
	def graficar(self):
		limit_i = -10
		limit_s = 10
		salto = 100
		x = np.array(self.pp_ene + self.pp_feb + self.pp_mar + self.pp_abr + self.pp_may + self.pp_jun + self.pp_jul + self.pp_ago + self.pp_sep + self.pp_oct + self.pp_nov + self.pp_dic)
		y = x**2
		
		self.mplwidget.axes.plot(x,y,'o-')
		
		self.mplwidget.axes.set_title('Historical Opening/Closing Prices')
		self.mplwidget.axes.set_xlabel('Date')
		self.mplwidget.axes.set_ylabel('Price')
		self.mplwidget.draw()
		self.mplwidget.axes.grid(True)
			

app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()


