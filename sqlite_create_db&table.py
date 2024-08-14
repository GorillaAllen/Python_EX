import sqlite3
con = sqlite3.connect("test.sqlite")

con.execute("""CREATE TABLE IF NOT EXISTS table01
            ("num" INTEGER PRIMARY KEY NOT NULL, "tel" TEXT)""")
    
con.execute('INSERT INTO table01 VALUES(1, "080")')
    
con.execute("""INSERT INTO table01(num, tel)
                VALUES(2,"020"),(3,"050")""")
                
con.commit()
con.close