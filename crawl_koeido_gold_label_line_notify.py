import requests as rq
from bs4 import BeautifulSoup as BS

url = r"http://koeido-mak.com/TIgs_list.htm"

response = rq.get(url)

soup = BS(response.text, "lxml")

td_tag = soup.find_all("font", color="#FF0000")

gold_item_list = []
for row in td_tag:
    if row.text == "New!":
        tag = row.find_previous("a") #取得前一個標籤
        gold_item_list.append(tag.text)



# ======================================
# Line Notify Setting
# ======================================
def notify(message, token):
    url = r"https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + token}
    payload = {'message': message # ,
                }
    rq.post(url, headers = headers,
                  params=payload)
    
message = """
"""
token = "6myNUFYNuyDExRpsF8fAYh9Alr2ICqSdsK6QrAcvymV"
for i in range(0, len(gold_item_list)):
    message += gold_item_list[i]

notify(message,token)