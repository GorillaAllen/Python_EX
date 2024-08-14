import sqlite3
con = sqlite3.connect("test.sqlite")
    
con.execute("""INSERT INTO table01(num, tel)
                VALUES(4,"040"),(5,"070")""")

#選定查詢區塊與建立游標物件
cur = con.execute('select * from table01 where num = 2')
rows = cur.fetchall()

#輸出全部
for i in rows:
    print("%2d | %s"%(i[0], i[1]))
                
con.commit()
con.close