from selenium import webdriver
import time, random
from bs4 import BeautifulSoup

driver=webdriver.Chrome()
driver.get("https://buyee.jp/item/search/query/%E5%85%89%E6%A0%84%E5%A0%82/seller/false/category/22436/?translationType=1")
driver.implicitly_wait(random.uniform(7.2, 13.6))


data = BeautifulSoup(driver.page_source, "lxml")

with open("getBuyee.html","w", encoding="utf8") as file:
    file.write(data.prettify())

time.sleep(random.uniform(7.2, 13.6))
driver.quit()
