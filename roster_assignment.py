import sqlite3
import json

conn = sqlite3.connect('roster_course.sqlite')
cur = conn.cursor()



cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
	name TEXT UNIQUE);

CREATE TABLE Course(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
	title TEXT UNIQUE);

CREATE TABLE Member (
    user_id  INTEGER ,
    course_id  INTEGER,
    role   INTEGER,
     PRIMARY KEY (user_id,course_id) )
	
	''' )

fname = 'roster_data.json'
str_data = open(fname).read()
data = json.loads(str_data)

for entry in data:
	name = entry[0]
	title = entry[1]
	role = entry[2]
	cur.execute('INSERT OR IGNORE INTO User(name) VALUES (?)', (name,))
	cur.execute('SELECT id FROM User WHERE name = ?', (name,))
	user_id = cur.fetchone()[0]
	cur.execute('INSERT OR IGNORE INTO Course(title) VALUES (?)', (title,))
	cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
	course_id = cur.fetchone()[0]
	cur.execute('''INSERT OR REPLACE INTO Member (user_id,course_id,role) 
		VALUES (?,?,?)''', (user_id,course_id,role) )

conn.commit()
















