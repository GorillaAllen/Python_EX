from bs4 import BeautifulSoup
import requests
# import pandas as pd

# # 網路上抓連結
url = "https://water.taiwanstat.com/"
response = requests.get(url)

try:
    response.raise_for_status()#確認給抓
    print("抓取成功\n--------------------------")
    data = response.content
    with open("reservoirInTaiwan.html", "wb") as file:#抓下原始html檔,存成local檔案
        file.write(data)
        
except Exception as err:
    print("Fail:", err)
    
    
    
with open("reservoirInTaiwan.html", encoding="UTF-8") as file1:#做成Beautifull Soup物件樹
    soup = BeautifulSoup(file1, "lxml")
    
tag1 = soup.find_all("h3")#在檔案裡找到需要抓的資料的標籤(需要的話,要包含class)

for row in tag1:
    print(row.text)
# print(productPriceList)
# print(tag.get_text("\n", strip=True))
