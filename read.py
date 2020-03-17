import sqlite3

db = sqlite3.connect('data.db')

rows = db.execute('SELECT * FROM users').fetchall()
print(rows)
