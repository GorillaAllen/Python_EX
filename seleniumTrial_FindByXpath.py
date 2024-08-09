from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
# from bs4 import BeautifulSoup
import os

driver=webdriver.Chrome()
url = os.path.abspath("getBuyee.html")
driver.implicitly_wait(random.uniform(7.2, 13.6))
driver.get(url)

tag = driver.find_element(By.CLASS_NAME, "itemCard")

# lst = []
for i in range(len(tag.tag_name)):
    tag_data = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/form/div[3]/ul/li["%d"]/div/div[2]/div[1]/a' %i+1)
    print(tag_data.text)
# for i in lst:
    # print(i)
    
driver.quit()
