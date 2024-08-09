from bs4 import BeautifulSoup
import requests
import pandas as pd

# # 網路上抓連結
# url = "https://www.gear4music.com/electric-guitars/manson?_gl=1*fcqdon*_up*MQ..*_ga*MjU1Nzc3MzUwLjE3MjEwMjkyNjU.*_ga_0WF1R5QW3K*MTcyMTAyOTI2NC4xLjEuMTcyMTAyOTI3NS4wLjAuMTQyMDk5NjY3Nw.."
# response = requests.get(url)

# try:
#     response.raise_for_status()#確認給抓
#     print("成功")
#     data = response.content
#     with open("g4m_manson_guitars.html", "wb") as file:#抓下原始html檔,存成local檔案
#         file.write(data)
        
# except Exception as err:
#     print("Fail:", err)
    
    
    
with open("g4m_manson_guitars.html", encoding="UTF-8") as file1:#做成Beautifull Soup物件樹
    soup = BeautifulSoup(file1, "lxml")
    
tag_name = soup.find("h3")#在檔案裡找到需要抓的資料的標籤(需要的話,要包含class)
tag_price = soup.find("div", class_="product-card-price")
all_data = soup.find_all("h3")
lst=[]
for row in all_data:
    name = tag_name.get_text(strip=True)
    price = tag_price.get_text(strip=True)
    lst.append([name,price])
    
print(lst)
data = pd.n
# print(productPriceList)
# print(tag.get_text("\n", strip=True))
