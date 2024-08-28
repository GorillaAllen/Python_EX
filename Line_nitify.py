import requests as rq
from bs4 import BeautifulSoup as BS

#======================================
# Line Notify Setting
#======================================
def notify(message, token, image):
    url = r"https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + token}
    payload = {'message': message # ,
              # "stickerPackageId": 7452,
                #"stickerId":1235469
                }
    image = open(image, "rb")
    imageFile = {"imageFile": image}
    rq.post(url, headers = headers,
                  data=payload, files=imageFile)
    
token = "6myNUFYNuyDExRpsF8fAYh9Alr2ICqSdsK6QrAcvymV"
message = "Jeff Beck!"
img = r"C:\Users\USER\Documents\jeff_beck_strat.jpg"
notify(message,token, img)