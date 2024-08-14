import sqlite3
con = sqlite3.connect("test_json.sqlite")
newdata = {"title": "Titanic","B_O": 2e5,"rank": 5}

con.execute('CREATE TABLE table01 IF NOT EXISTS(title TEXT, B_O INT, rank INT)')

sql = "INSERT INTO table01 (title, B_O, rank) VALUES('{}','{}','{}')"
sql = sql.format(newdata["title"], newdata["B_O"], newdata["rank"])
con.execute(sql)


#選定查詢區塊與建立游標物件
cur = con.execute('select * from table01')
rows = cur.fetchall()

#輸出全部
for i in rows:
    print("%10s | %s | %d"%(i[0], i[1], i[2]))
                
con.commit()
con.close