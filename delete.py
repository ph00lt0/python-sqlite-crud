import sqlite3

db = sqlite3.connect('data.db')

db.execute('DELETE FROM users WHERE id = ?', ('cb18f292-9810-4e39-9b0e-d40953b35d69',))
db.commit()
