from xml.dom import minidom
import os
import pandas as pd
import pymysql as MySQLdb

# 用os.listdir()查詢data資料夾裡有幾個檔案
dirpath = r"C:\Users\USER\Desktop\python workspace\data"
allfile = os.listdir(dirpath)

newdata = []

# 用迴圈讀取XML內的資料
for i in range(len(allfile)):
    fp = dirpath + "\\" + allfile[i]
    # 解析XML文件   
    tree = minidom.parse(fp)
    # 找到所有<EarthquakeInfo>節點
    earthquake_info = tree.getElementsByTagName("EarthquakeInfo")
    # 進入每一個<EarthquakeInfo>節點後
    # 找出每個地震的發生時間、緯(lat)經(lon)度
    for child in earthquake_info:
        timevalue = child.getElementsByTagName("OriginTime")[0].firstChild.nodeValue
        latitude = child.getElementsByTagName("EpicenterLatitude")[0].firstChild.nodeValue
        longitude = child.getElementsByTagName("EpicenterLongitude")[0].firstChild.nodeValue
        magni = child.getElementsByTagName("LocalMagnitude")[0].firstChild.nodeValue
        
        # 將資料放入list中
        newdata.append([timevalue[:10], timevalue[11:19], latitude, longitude, magni])
    
    
alldata = pd.DataFrame(newdata)
del newdata

# # 連接SQL並寫入
try:
    # 開啟資料庫連接
    conn = MySQLdb.connect(host="localhost",     # 主機名稱
                            user="root",        # 帳號
                            password="9527", # 密碼
                            database = "bill", #資料庫
                            port=3306,
                            charset="utf8")           # port
    
    # 使用cursor()方法操作資料庫
    cursor = conn.cursor()
    
    # 將alldata的資料寫到資料庫
    try:
        for i in range(len(alldata)):
            sql = """INSERT INTO earthquake (date, time, lat, lon, magnitude)
                                    VALUES (%s, %s, %s, %s, %s)"""
            var = (alldata.iloc[i,0], alldata.iloc[i,1], alldata.iloc[i,2], alldata.iloc[i,3], alldata.iloc[i,4])     
            cursor.execute(sql, var)
            
        conn.commit()
        print("資料寫入完成")
        
        cursor.close()
        conn.close()
       
    except Exception as e:
        print("錯誤訊息：", e)
 

except Exception as e:
    print("資料庫連接失敗：", e)
    
finally:
    print("資料庫連線結束")