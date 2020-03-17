import sqlite3

db = sqlite3.connect('data.db')

rows = db.execute('SELECT * FROM users').fetchall()
rows = [dict(zip(["id", "name"], row)) for row in rows]
print(rows)
