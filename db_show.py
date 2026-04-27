import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

cur.execute("SELECT * FROM pdfs")
print(cur.fetchall())

conn.close()
