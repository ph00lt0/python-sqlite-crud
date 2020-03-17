import sqlite3
import uuid

db = sqlite3.connect('data.db')

id = str(uuid.uuid4())
name = "ABC"

db.execute('INSERT INTO users VALUES(?,?)',(id, name))
db.commit()
