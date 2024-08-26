import requests, os, urllib,re
from bs4 import BeautifulSoup
url= r"http://koeido-mak.com/TIgs_list.htm"
#用requests取得網頁文本
html=requests.get(url)
html.encoding="utf8"
#用beautiful解析
bs=BeautifulSoup(html.text, r"html.parser")
pics_dir="pics"

#建立資料夾
if not os.path.exists(pics_dir):
    os.mkdir(pics_dir)
    
#搜尋有'a'的html標籤.
name_list = []
all_links=bs.find_all('a')
for link in all_links:
    #取得有含有'href'字串的標籤的內容
    src=link.get('href')
    if  isinstance(src, str):
        if ".htm" in src:
            name_list.append(src)
            
url_list = []
for name in name_list:
    url_list.append(r"http://koeido-mak.com/" + name)

# print(url_list)

pre_img_url_list = []
for url in url_list:
    html=requests.get(url)
    bs=BeautifulSoup(html.text, r"html.parser")
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

# for img_url in img_url_list:
#     html_img=requests.get(img_url)
#     bs_img = BeautifulSoup(html_img.text, r"html.parser")
#     img_links = bs_img.findall('a')
    
    