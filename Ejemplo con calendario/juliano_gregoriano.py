#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
======================================================================
Funciones: 

Juliano_gregoriano es una biblioteca utilizada en la conversion de los 
dias de calendario de tipo julianos a gregoriano , o viceversa ,  
solo si el anio es bisiesto. 
======================================================================
"""

__author__ = "Carlos Hernandez <carlitoshernandez20@gmail.com>"
__version__ = "1.0"
__date__ = "Mayo 2015"

def conv_juliano_gregoriano(fecha_juliana,anio):
	"""
	==================================================================
	Funcion para la conversion de  los dias del calendario gregoriano 
	en dias del calendario juliano, solo si el anio es bisiesto 
	==================================================================
	Funciones : 
		- gregoriano_juliano() : Funcion de conversion 
			calendario gregoriano > calendario juliano
					
	Ejemplos:
		>>> conv_juliano_gregoriano(34,2015)
		3/Feb/2005	
		>>> conv_juliano_gregoriano(122,1993)
		2/May/1993
			
	
	Parametros:
		- Fecha juliana en valor que va desde 0 a 365	
		
	Retornos:
		- Fecha de tipo de calendario Gregoriano en formato dd/mm/anio		
			
	"""				
	dia = fecha_juliana
						
	if (dia >= 0 and dia <= 31) :
		mes = "Ene"
	elif (dia > 31 and dia <= 59) :
		mes = "Feb"
	elif (dia > 59 and dia <= 90) :
		mes = "Mar"
	elif (dia >= 90 and dia <= 120) :
		mes = "Abr"
	elif (dia >= 120 and dia <= 151) :
		mes = "May"
	elif (dia >= 151 and dia <= 181) :
		mes = "Jun"
	elif (dia >= 181 and dia <= 212) :					
		mes = "Jul"
	elif (dia >= 212 and dia <= 243) :					
		mes = "Ago"
	elif (dia >= 243 and dia <= 273) :					
		mes = "Sep"
	elif (dia >= 273 and dia <= 304) :					
		mes = "Oct"			
	elif (dia >= 304 and dia <= 334) :					
		mes = "Nov"
	elif (dia >= 334 and dia <= 365) :					
		mes = "Dic"		
	else:
		"Ha ocurrido un error - Ingrese correctamente los dias julianos desde 0 a 365"
		
	
	
	if (mes == "Ene"):
		dia_mes =  fecha_juliana 
	elif (mes == "Feb"):
		dia_mes = fecha_juliana - 31
	elif (mes == "Mar"):
		dia_mes =  fecha_juliana - 59
	elif (mes == "Abr"):
		dia_mes =  fecha_juliana - 90 
	elif (mes == "May"):
		dia_mes =  fecha_juliana - 120
	elif (mes == "Jun"):
		dia_mes =  fecha_juliana - 151
	elif (mes == "Jul"):
		dia_mes =  fecha_juliana - 181
	elif (mes == "Ago"):
		dia_mes =  fecha_juliana  -212
	elif (mes == "Sep"):
		dia_mes =  fecha_juliana - 243
	elif (mes == "Oct"):
		dia_mes  = fecha_juliana - 273
	elif (mes == "Nov"):
		dia_mes =  fecha_juliana - 304
	elif (mes == "Dic"):
		dia_mes =  fecha_juliana - 334
	
	dia_mes10 = str(dia_mes)
	mes10 = str(mes)
	anio10 = str(anio)
	esp = "/"	
	return  dia_mes10 +esp+ mes10 + esp + anio10
	
	

def conv_gregoriano_juliano(fecha_gregoriana):
	

	
	""" 
	==================================================================
	Funcion para la conversion de  los dias del calendario gregoriano 
	en dias del calendario juliano ,solo si el anio es bisiesto.
	==================================================================
	Funciones : 
			- gregoriano_juliano() : Funcion de conversion 
				calendario gregoriano > calendario juliano
					
	Ejemplos:
			>>> conv_gregoriano_juliano("Dom Dic 31 2015")
			365	
			>>> conv_gregoriano_juliano("Dom Feb 3 2015")
			34
					
	Parametros:
		- Fecha gregoriana en formato DD/dd/mm/yy 
		
	Retornos:
		- Dia Juliano en un valor que vas desde 0 a 365	
	"""
	
	dia = str(fecha_gregoriana)
	mes = fecha_gregoriana[4:7]
	dia1 = int(fecha_gregoriana[8:10])
	
	
	if (mes == "Ene"):
		dias = 0
	elif (mes == "Feb"):
		dias = 31
	elif (mes == "Mar"):
		dias = 59
	elif (mes == "Abr"):
		dias = 90
	elif (mes == "May"):
		dias = 120
	elif (mes == "Jun"):
		dias = 151
	elif (mes == "Jul"):
		dias = 181
	elif (mes == "Ago"):
		dias = 212
	elif (mes == "Sep"):
		dias = 243
	elif (mes == "Oct"):
		dias = 273
	elif (mes == "Nov"):
		dias = 304
	elif (mes == "Dic"):
		dias = 334
		
	dia_juliano = dias + dia1
	return dia_juliano
	
#Ejemplos	
#print conv_gregoriano_juliano("Lun May 3 2015")
#print "\n"	
#print conv_juliano_gregoriano(122,2015)	
	
		
	


