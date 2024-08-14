import sqlite3
conn = sqlite3.connect("test.sqlite")

cursor = conn.execute('select * from table01')

rows = cursor.fetchall()

for i in rows:
    print("%2d | %s"%(i[0], i[1]))
conn.close

newrow = cursor.fetchone()

print(newrow)