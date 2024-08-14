import csv
import sqlite3
con = sqlite3.connect("111 population desity.sqlite")
con.execute("""CREATE TABLE IF NOT EXISTS table01
            ("統計年" TEXT, "區域別" TEXT,"年底人口數" TEXT,
            "土地面積" TEXT, "人口密度" TEXT)""")

indata = "111年各鄉鎮市區人口密度.csv"
with open(indata, encoding ="utf-8") as file: #取得檔案物件
    readfile = csv.reader(file)
    data = list(readfile)
    

new_line = []
new_data = []         
for i in range (0, 371):
    new_line = []
    for j in range(0,5):
        new_line.append(data[i][j])
    new_data.append(new_line)
    
for i in range(0, len(new_data)):  
    sql = 'INSERT INTO table01 (統計年,區域別,年底人口數,土地面積,人口密度) VALUES("{}","{}","{}","{}","{}")'
    sql = sql.format(new_data[i][0], new_data[i][1], new_data[i][2], new_data[i][3], new_data[i][4])
    con.execute(sql)

#選定查詢區塊與建立游標物件
cur = con.execute('select * from table01')
# rows = cur.fetchall()

#輸出全部
# for i in rows:
#     print("%8s%8s%8s%8s%8s"%(i[0], i[1], i[2], i[3], i[4]))

for i in range(6):
    newrow = cur.fetchone()
    print(newrow)
    
con.commit()
con.close
file.close()