#!/usr/bin/python
# -*- coding:utf-8 -*-

import sqlite3



def connectDB(dbFile):
	conn = sqlite3.connect(dbFile)
	cur = conn.cursor()
	return conn,cur

conn, cur = connectDB("mp3DB.sqlite")

def addSong():
	title = raw_input("\n\tIntroduzca el titulo\t")
	author = raw_input("\n\tIntroduzca el autor\t")
	time = raw_input("\n\tIntroduzca la duración\t")
	style = raw_input("\n\tIntroduzca el estilo\t")
	sql = "INSERT INTO MP3 (titulo, interprete, duracion, estilo) VALUES ((?), (?), (?), (?));"
	song = cur.execute(sql, (title, author, time, style))
	conn.commit()
	print("\nCanción añadida")

def showStyles():
	sql = "SELECT estilo FROM MP3"
	allStyles = cur.execute(sql)
	styles = []
	for i in allStyles:
		styles.append(i)
		print("\n\t"+str(i))

def showAuthorSongs():
	author = raw_input("\n\tIntroduzca un autor\t")
	sql = "SELECT titulo FROM MP3 WHERE interprete=(?)"
	authorSongs = cur.execute(sql, (author, ))
	songs = []
	for i in authorSongs:
		songs.append(i)
		print("\n\t"+str(i))

def showStyleSongs():
	style = raw_input("\n\tIntroduzca un estilo\t")
	sql = "SELECT titulo FROM MP3 WHERE estilo=(?)"
	styleSongs = cur.execute(sql, (style, ))
	songs = []
	for i in styleSongs:
		songs.append(i)
		print("\n\t"+str(i))

def selectAll():
	sql = "SELECT * FROM MP3"
	allSongs = cur.execute(sql)
	songs = []
	for i in allSongs:
		songs.append(i)
		print("\n\t"+str(i))

def deleteSong():
	title = raw_input("\n\tIntroduzca un titulo\t")
	author = raw_input("\n\tIntroduzca un autor\t")
	sql = "DELETE FROM MP3 WHERE titulo=(?) AND interprete=(?)"
	song = cur.execute(sql, (title, author))
	print("\nEliminación completada")


