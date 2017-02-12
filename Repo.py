#!/usr/bin/python
# -*- coding:utf-8 -*-

import sqlite3



def connectDB(dbFile):
	conn = sqlite3.connect(dbFile)
	cur = conn.cursor()
	return conn,cur

conn, cur = connectDB("mp3DB.sqlite")

def selectAll():
	sql = "SELECT * FROM MP3"
	allSongs = cur.execute(sql)
	songs = []
	for i in allSongs:
		songs.append(i)
	return songs

print selectAll()
