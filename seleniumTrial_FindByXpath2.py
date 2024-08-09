from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
# from bs4 import BeautifulSoup
import os

driver=webdriver.Chrome()
driver.implicitly_wait(random.uniform(7.2, 13.6))
driver.get("https://24h.pchome.com.tw/")

search = driver.find_element(By.CLASS_NAME, "l-header__siteSearchInput")

driver.implicitly_wait(random.uniform(7.2, 13.6))

search.click

search.send_keys("python")

#
driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div[1]/div/div/div/div[1]/div[2]/input')
    
driver.quit()
