import requests, os, urllib
from bs4 import BeautifulSoup
url= "http://koeido-mak.com/TIgs_list.htm"
html=requests.get(url)
html.encoding="utf8"
bs=BeautifulSoup(html.text, "html.parser")
pics_dir="pics"
if not os.path.exists(pics_dir):
    os.mkdir(pics_dir)
    
all_links=bs.find_all('img')
for link in all_links:
    src=link.get('src')
    attrs=[src]
    for attr in attrs:
        if attr!=None and('.jpg' in attr or'.png' in attr):
            full_path = attr
            file_n=full_path.split('/')[-1]
            print('----------------')
            print("full path:", full_path)
            try:
                image = urllib.request.urlopen(full_path)
                f = open(os.path.join(pics_dir, file_n),'wb')
                f.write(image.read())
                print("download success:%s"%(file_n))
                f.close()
            except:
                print("fail:"%(file_n))