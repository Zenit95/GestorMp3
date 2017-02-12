#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

 
options = ["Añadir nueva cancion", "Listar estilos", "Listar canciones - Autor", "Listar canciones - Estilo",
			 "Listar todas las canciones", "Eliminar cancion", "Salir"]




def printMenu():

	os.system('clear') 	#Función que limpia la pantalla y muestra nuevamente el menu

	print ("*****************************")
	print ("          GESTOR MP3         ")
	print ("*****************************")

	print ("Selecciona una opción")

	for i in range(len(options)):
		print("\t" +  str(i+1) + ". "+ options[i])

def menu():

 	printMenu()



 

while True:

	# Mostramos el menu

	menu()

 

	# solicituamos una opción al usuario

	opcionMenu = input("inserta un numero valor >> ")

 




	if opcionMenu==1:

		print ("")

		input("Has pulsado la opción 1...\npulsa una tecla para continuar")

	elif opcionMenu==2:

		print ("")

		input("Has pulsado la opción 2...\npulsa una tecla para continuar")

	elif opcionMenu==3:

		print ("")

		input("Has pulsado la opción 3...\npulsa una tecla para continuar")

	elif opcionMenu==4:

		print ("")

		input("Has pulsado la opción 4...\npulsa una tecla para continuar")

	elif opcionMenu==5:

		print ("")

		input("Has pulsado la opción 5...\npulsa una tecla para continuar")

	elif opcionMenu==6:

		print ("")

		input("Has pulsado la opción 6...\npulsa una tecla para continuar")

	elif opcionMenu==9:

		break

	else:

		print ("")

		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")





