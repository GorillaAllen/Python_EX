import requests
import pandas as pd
#下載網頁
url = "https://www.gear4music.com/"
response = requests.get(url)

try:
    response.raise_for_status()
    print("成功")
    data = response.content
    with open("g4m.html", "wb") as file:
        file.write(data)
        
except Exception as err:
    print("Fail:", err)
