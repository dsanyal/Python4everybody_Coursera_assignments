import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
fname = 'mbox.txt'
f = open(fname)

for line in f:
	if not line.startswith('From '): continue
	words = line.split()
	domain = words[1].split('@')[1]
	cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,) )
	row = cur.fetchone()
	if row is None:
		cur.execute('INSERT INTO Counts(org,count) VALUES (?,1)' , (domain,) )
	else:
		cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (domain,) )	
conn.commit()
sqlfetch = 'SELECT * FROM Counts ORDER BY count DESC'
for row in cur.execute(sqlfetch):
	print(str(row[0]), row[1])
cur.close()
f.close()
