#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, Repo, sys

 
options = ["Añadir nueva cancion", "Listar estilos", "Listar canciones - Autor", "Listar canciones - Estilo",
			 "Listar todas las canciones", "Eliminar cancion", "Salir"]
functions = [Repo.addSong, Repo.showStyles, Repo.showAuthorSongs, Repo.showStyleSongs, Repo.selectAll, Repo.deleteSong, exit]



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

def exit():
	global cur, conn
	cur.close()
	conn.close()

while True:

	menu()	

 	opcionMenu = input("Opcion seleccionada >> ")

	print("\n" + options[opcionMenu-1])
	
	functions[opcionMenu-1]()

	raw_input()






