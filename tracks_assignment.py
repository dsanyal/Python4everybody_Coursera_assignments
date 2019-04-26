import sqlite3
import xml.etree.ElementTree as ET


conn = sqlite3.connect('tracksdb.sqlite')
cur = conn.cursor()



cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
	name TEXT UNIQUE);

CREATE TABLE Genre(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
	name TEXT UNIQUE);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
	title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER)
	''')

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None


tree = ET.parse('tracks/Library.xml')
library = tree.findall('dict/dict/dict')
print('Dict count:', len(library))

for entry in library:
	if lookup(entry, 'Track ID') is None : continue
	trackname = lookup(entry, 'Name')
	artist = lookup(entry, 'Artist')
	album = lookup(entry, 'Album')
	genre = lookup(entry, 'Genre')
	count = lookup(entry, 'Play Count')
	rating = lookup(entry, 'Rating')
	length = lookup(entry, 'Total Time')

	if trackname is None or artist is None or genre is None or album is None : continue

	cur.execute('INSERT OR IGNORE INTO Artist(name) VALUES (?)', (artist,) )
	cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
	artist_id = cur.fetchone()[0]

	cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES (?)', (genre,) )
	cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
	genre_id = cur.fetchone()[0]

	cur.execute('INSERT OR IGNORE INTO Album(title,artist_id) VALUES (?,?)', (album, artist_id) )
	cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
	album_id = cur.fetchone()[0]

	cur.execute('''INSERT OR REPLACE INTO Track(title, album_id,
    	genre_id, len, rating, count) 
        VALUES (?,?,?,?,?,?)''',  (trackname, album_id,genre_id,length,rating,count) )

conn.commit()










