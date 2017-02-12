#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, Repo

 
options = ["Añadir nueva cancion", "Listar estilos", "Listar canciones - Autor", "Listar canciones - Estilo",
			 "Listar todas las canciones", "Eliminar cancion", "Salir"]
functions = [Repo.selectAll]



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

	menu()	

 	opcionMenu = input("inserta un numero valor >> ")


	print("\n" + options[opcionMenu-1])
	
	print functions[opcionMenu-1]()

	raw_input()






