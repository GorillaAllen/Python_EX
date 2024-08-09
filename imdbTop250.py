from bs4 import BeautifulSoup
import requests
# import pandas as pd

# 網路上抓連結
url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

try:
    response.raise_for_status()#確認給抓
    print("抓取成功\n--------------------------")
    data = response.content
    with open("imdbTop250.html", "wb") as file:#抓下原始html檔,存成local檔案
        file.write(data)
        
except Exception as err:
    print("Fail:", err)
    
    
    
with open("imdbTop250.html", encoding="UTF-8") as file1:#做成Beautifull Soup物件樹
    soup = BeautifulSoup(file1, "lxml")
    
#方法1:直接在檔案裡找到需要抓的資料的標籤(需要的話,要包含class). 但有可能因為"不要的資料的標籤"跟"要的資料的標籤一樣"導致資料不精確
tag1 = soup.find_all("h3", limit = 250)
#以get_text(strip=True)取得已經去除無意義空行的字串
lst=[]
for row in tag1:
    lst.append(row.get_text(strip=True))
for i in lst:
    print(i)

#其他方法: 先以.find()取得包含所有需要的text的上層標籤
# data = soup.find("div", class_="post-hot stories-container")
#再以.find_all()來搜尋該上層標籤下的所有text
# lst = []
# for row in data.find_all("h2"):
#     lst.append(row.get_text(strip=True))

# for i in lst:
#     print(i)
