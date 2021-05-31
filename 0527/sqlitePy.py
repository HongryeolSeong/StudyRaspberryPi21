import sqlite3

dbconn = sqlite3.connect('./tesdb.db')
cursor = dbconn.cursor()

try:
	cursor.execute("CREATE TABLE if not exists user(id INTEGER, name text, phone text, sex text)")
	cursor.execute("INSERT INTO user(id, name, phone, sex) VALUES(1, 'hong', '010-7759-0276', 'm')")
	cursor.execute("INSERT INTO user(id, name, phone, sex) VALUES(2, 'yeong', '010-1234-1234', 'm')")
	cursor.executemany("insert into user(id, name, phone, sex) values(?, ?, ?, ?)",\
		[(3, 'kim', '010-1111-1111', 'm'), (4, 'seol', '010-2222-2222', 'm'), (5, 'soe', '010-5209-0276', 'f')])

	dbconn.commit()
except KeyboardInterrupt:
	dbconn.close()
