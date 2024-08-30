import requests, os, urllib,re
import requests as rq
from bs4 import BeautifulSoup as BS

pics_dir="new gold item pics"
#建立資料夾
if not os.path.exists(pics_dir):
    os.mkdir(pics_dir)

url = r"http://koeido-mak.com/TIgs_list.htm"
response = rq.get(url)
soup = BS(response.text, "lxml")
td_tag = soup.find_all("font", color="#FF0000")

#想要的字串在有"NEW!"字串的標籤的前面一個 
gold_item_list = []
individual_gold_item_link_list = []
for row in td_tag:
    if row.text == "New!":
        tag = row.find_previous("a") #取得前一個標籤
        gold_item_list.append(tag.text)
        link = tag.get('href')
        individual_gold_item_link_list.append(link)
# print(individual_gold_item_link_list)

url_list = []
for name in individual_gold_item_link_list:
    url_list.append(r"http://koeido-mak.com/" + name)
# print(url_list)

pre_img_url_list = []
for url in url_list:
    html=requests.get(url)
    bs=BS(html.text, r"html.parser")
    img_links=bs.find_all('img')
    for link in img_links:
        img_src=link.get('src')
        pre_img_url_list.append(img_src)
        
img_url_list = []
for pre_img_url in pre_img_url_list:
    img_url_list.append(r"http://koeido-mak.com/" + pre_img_url)
        
for img_url in img_url_list:
    if img_url!=None and('.jpg' in img_url or'.png' in img_url):
        full_path = img_url
        file_n=full_path.split('/')[-1]
        print('----------------')
        print("full path:", full_path)
        try:
            image = urllib.request.urlopen(full_path)
            # print("success")
            f = open(os.path.join(pics_dir, file_n),"wb")
            f.write(image.read())
            print("download success:%s"%(file_n))
            f.close()
        except:
            print("fail")



# ======================================
# Line Notify Setting
# ======================================
token = "6myNUFYNuyDExRpsF8fAYh9Alr2ICqSdsK6QrAcvymV"

def notify_message(message, token):
    url = r"https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + token}
    payload = {'message': message # ,
              # "stickerPackageId": 7452,
                #"stickerId":1235469
                }
    rq.post(url, headers = headers,
                  params=payload)

def notify_image(empty_message, token, image):
    url = r"https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + token}
    payload = {'message': message # ,
              # "stickerPackageId": 7452,
                #"stickerId":1235469
                }
    rq.post(url, headers = headers,
                  params=payload)
    image = open(image, 'rb')
    imageFile = {"imageFile": image}
    rq.post(url, headers = headers, data=payload,
                  files=imageFile)


for i in range(0, len(pre_img_url_list)):
    message = """
    """
    for i in range(0, len(gold_item_list)):
        message += gold_item_list[i] + '\n'
    notify_message(message,token)
    
    
empty_message=""
for i in range(0, len(pre_img_url_list)):
    img = r'C:\Users\USER\Desktop\python workspace\new gold item pic'
    
    
    notify_image(message,token,img)
    
pre_img_url_list  
img = r"C:\Users\USER\Documents\jeff_beck_strat.jpg"




    
notify_image(empty_message,token, img)