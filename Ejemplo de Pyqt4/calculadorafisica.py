#!/usr/bin/env python
#-*- coding: utf-8 -*-
print '\t\t\tCalculadora para Fisica'
print '\n\t\t      Creada en python by Carlitos Hernandez'
print '\n'

from math import sqrt , pi
import os

opcion=13
velocidad_angular=""
velocidad_tangencial=""
radio=""
diametro=""
altura=""
densidad=""
gravedad=""
presion=""

os.system('title calculadora-cientifica')
os.system('color 03')

while opcion > 1 or opcion < 12 :
	print('Elija la opcion :\n\t1.-velocidad angular\t\t2.-velocidad tangencial\n\t3.-Aceleracion centripeta\t4.-Aceleracion tangencial\n\t5.-Aceleracion angular\t\t6.-Fuerza centripeta\n\t7.-Trabajo de una fuerza\t8.-Potencia\n\t9.-Presion\t\t\t10.-Caudal\n\t11.-Salir')
	opcion=int(raw_input("\nIntrodusca la opcion que nesecita  >>> "))
	
	if(opcion==1):
		#
		print('\nVelocidad angular')
		angulo_barrido=float(raw_input("\ningrese el angulo barrido en radianes :"))
		tiempo_barrido=float(raw_input("ingrese el tiempo de barrido en segundos :"))
		w=(angulo_barrido)/(tiempo_barrido)
		print '\nLa velocidad angular es :',w ,"rad/seg"			
		  
		
	elif(opcion==2):
		#
		print('\nVelocidad Tangencial')
		velocidad_angular2=float(raw_input("Ingrese la velocidad angular en m/s :"))
		radio2 =float(raw_input("Ingrese el radio en metros :"))
		velocidad_tangencial1=velocidad_angular2*radio2
		print "\nLa velocidad tangencial es :",velocidad_tangencial1,"m/s"
	
	elif(opcion==3):
		#aceleracion centripeta
		print('\nAceleracion centripeta')
		velocidad_angular3=float(raw_input("\nIngrese la velocidad angular en rad/seg: "))
		radio3=float(raw_input("\nIngrese el radio en metros: "))
		aceleracion_centripeta=(velocidad_angular3**velocidad_angular3)*radio3
		print "\nLa Aceleracion centripeta es :",aceleracion_centripeta,"m/seg^2"
		
	elif(opcion==4):	
		#Aceleracion tangencial
		print('\nAceleracion tangencial')
		radio4=float(raw_input("Ingrese el radio en metros :"))
		aceleracion_angular2=float(raw_input("\nIngrese la aceleracion angular en rad/seg^2 :"))
		aceleracion_tangencial=radio4*aceleracion_angular2
		print "\nLa aceleracion tangencial es de :",aceleracion_tangencial,"m/seg^2"
	
	elif(opcion==5):
		#Aceleracion angular
		print('\nAceleracion angular')
		velocidad_angular4=float(raw_input("\nIngrese la velocidad angular en rad/seg"))
		tiempo=float(raw_input("\nIngrese el tiempo en segundos :"))
		aceleracion_angular3 = velocidad_angular4 * tiempo
		print '\nLa aceleracion angular es de :',aceleracion_angular3,"rad/seg^2"	
	
	elif(opcion==6):
		#Fuerza centripeta
		print("\nFuerza Centripeta")
		masa=float(raw_input("\nIngrese la masa del objeto en kg-fuerza :"))
		aceleracion_centripeta2=float(raw_input("\nIngrese la acelracion centripeta en m/s^2 :"))
		fuerza_centripeta=masa*aceleracion_centripeta2
		print '\nLa fuerza centripeta es :',fuerza_centripeta,"N"
		
	elif(opcion==7):
		#Trabajo de una fuerza
		print("Trabajo de una fuerza")
		fuerza=float(raw_input("\nIngrese la fuerza en Newton: "))
		distancia=float(raw_input("\nIngresa la distancia en metros: "))
		cose=float(raw_input("\nIngrese el angulo respecto de la accion de la fuerza: "))
		trabajo=fuerza*distancia*coseno(cose)
		print '\nEl trabajo realizado es de :',trabajo,"joule"
		
	elif(opcion==8):
		
		#potencia			
		print("\nPotencia")
		trabajo1=float(raw_input("\nIngrese el trabajo en joule :"))
		velocidad=float(raw_input("\nIngrese la velocidad en m/s :"))
		potencia=trabajo1*velocidad
		potencia_hp=potencia/746
		print'\nLa potencia es de :',potencia_hp,"Hp"
		
	elif(opcion==9):
		
		#Presion
		print("\nPresion")
		fuerza1=float(raw_input("\nIngrese la fuerza en Newton :"))
		angulo_aplicacion=int(raw_input("\nIngrese el angulo de aplicacion :"))
		superficie=int(raw_input("Ingrese la superficie en m^2 :"))
		presion =(fuerza1*cos(angulo_aplicacion))/superficie
		print '\nLa presion es de :',presion,"Pascal"
	
	elif(opcion==10):
		
		#Caudal
		opcion2=raw_input("Conoce el diametro del tubo? :")
		if(opcion2=="si"):
			diametro=int(raw_input("\nIngresa el diametro del orificio en metros: "))
			altura=int(raw_input("\nIngresa la altura del nivel del liquido en metros: "))
			ecuacion_bernoulli=float(((pi*(diametro**diametro))/4)* sqrt(2*9,8*altura))
			print '\nEl caudal es de :',ecuacion_bernoulli,"m^3/seg"
		else:
			
			radio5=int(raw_input("\nIngresa el radio del orificio en metros: "))	
			altura=int(raw_input("\nIngresa la altura del nivel del liquido: "))
			ecuacion_bernoulli=float((( pi *(radio5**radio5))/4)* sqrt(2*9,8*altura))
			print '\nEl caudal es de :',ecuacion_bernoulli,"m^3/seg"
	
		
	elif(opcion==11): 
		#Salir
		
		print"\n\tGracias por usar mi pequena calculadora"
		print"\nSi desea salir presione enter"
		print '\n\n\t\tRedondeandoainfinito.blogspot.com.ar'
		print'\n\n'
		exit()	
		
	else:
		print 'No válido'
		print '\n\n\n'
	print '\n\n\t\tRedondeandoainfinito.blogspot.com.ar'
	print '\n\n'

