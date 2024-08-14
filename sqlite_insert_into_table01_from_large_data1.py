import sqlite3
con = sqlite3.connect("test.sqlite")
newdata = '7,090'
f_newdata = newdata.split(",")
    

sql = "INSERT INTO table01 (num, tel) VALUES('{}','{}')"
sql = sql.format(f_newdata[0], f_newdata[1])
con.execute(sql)


#選定查詢區塊與建立游標物件
cur = con.execute('select * from table01')
rows = cur.fetchall()

#輸出全部
for i in rows:
    print("%2d | %s"%(i[0], i[1]))
                
con.commit()
con.close