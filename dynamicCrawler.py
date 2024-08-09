from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

try:
  
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.nba.com/stats/players/traditional")
    driver.maximize_window()#視窗最大化
    
    page = 1
    
    while True:        
        soup = BeautifulSoup(driver.page_source, "lxml") #解析網頁的html.soup是物件樹
        
        # 確認目前總頁數
        pageloc = soup.find("div", {"class":"Pagination_content__f2at7 Crom_cromSetting__Tqtiq"}) #鎖定html檔的某個標籤
        page_num = pageloc.find_all("div") #找此標籤下的子標籤
        totalpage = page_num[6].text.split(" ")[1] #要的資料在page_num標籤下的第[6]個標籤,用text取內容str,用split()切成list,取[1]
        
        # 先找到存放NBA球員資料的table
        table = soup.select_one("#__next > div.Layout_base__6IeUC.Layout_withSubNav__ByKRF.Layout_justNav__2H4H0 > \
                            div.Layout_mainContent__jXliI > div.MaxWidthContainer_mwc__ID5AG > \
                            section.Block_block__62M07.nba-stats-content-block > div > \
                            div.Crom_base__f0niE > div.Crom_container__C45Ti.crom-container")
        
        # 將球員資料放到dataframe中再寫成csv檔
        df = pd.read_html(str(table))
        df[0].to_csv("NBA球員資料第%d頁.csv" %page)
        print("正在儲存第%d頁..." %page)               
        
        try:
            # csv檔下載完畢後等待2秒再按下下一頁的按鈕
            time.sleep(2)    
            driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[5]/button[2]').click()
            
            # 判定是否按到最後一頁
            if page < int(totalpage):
                page += 1                
                continue
            else:
                print("下載完畢")
                break
        
        except Exception as e:
            print("下載失敗：", e)    
                                       
except Exception as e:
    print("爬取失敗：", e)

finally:
    driver.quit() 
