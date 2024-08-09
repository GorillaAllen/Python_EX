from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
# from bs4 import BeautifulSoup
import os

driver=webdriver.Chrome()
url = os.path.abspath("getBuyee.html")
driver.implicitly_wait(random.uniform(7.2, 13.6))
driver.get(url)

tags = driver.find_elements(By.CLASS_NAME, "itemCard__itemName")
lst = []
for tag in tags:
    lst.append(tag.get_text(strip=True))
for i in lst:
    print(i)
    
driver.quit()
