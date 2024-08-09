import requests
import pandas as pd
#下載圖片

#url在網頁瀏覽器的按F12獲得網頁資料後,選Networl的tag,找圖片連結
url = "https://guitarchimp.com/cdn/shop/files/IMG_1593_b4273fc4-2874-4e52-a1c9-b53cc007f72a.jpg?v=1686720622"
response = requests.get(url)

try:
    response.raise_for_status()
    print("成功")
    data = response.content
    with open("gretsch_g6131.html", "wb") as file:
        file.write(data)
        
except Exception as err:
    print("Fail:", err)
