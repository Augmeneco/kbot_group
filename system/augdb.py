#AugDB ПРИНАДЛЕЖИТ КЕкерУ. НИ ПИЗДИТЬ
import sqlite3
def create(name,table,data):
	conn = sqlite3.connect(name)
	cursor = conn.cursor()
	cursor.execute("""CREATE TABLE """+table+"""
				  ("""+data+""")
				""")
	conn.commit()
def read(name,table,data):
	conn = sqlite3.connect(name)
	cursor = conn.cursor()
	sql = "SELECT * FROM "+table+" WHERE "+data
	cursor.execute(sql)
	return cursor.fetchall()
def write(name,table,data):
	conn = sqlite3.connect(name)
	cursor = conn.cursor()
	val = '('+'?,'*len(data[0])+')'
	val = val.replace(',)',')')
	cursor.executemany("INSERT INTO "+table+" VALUES "+val, data)
	conn.commit()
def replace(name,table,where,setd):
	conn = sqlite3.connect(name)
	cursor = conn.cursor()
	sql = """
UPDATE """+table+""" 
SET """+setd+""" 
WHERE """+where
	cursor.execute(sql)
	conn.commit()
def remove(name,table,data):
	conn = sqlite3.connect(name)
	cursor = conn.cursor()
	sql = "DELETE FROM "+table+" WHERE "+data
	cursor.execute(sql)
	conn.commit()