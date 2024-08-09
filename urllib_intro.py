import urllib

url = "https://cuiqingcai.com/indea.html"

try:
    # 訪問一個不存在的頁面
 	response = urllib.request.urlopen(url)
    
except urllib.error.HTTPError as e:
    # 顯示錯誤的原因
 	print(e.reason)
    # 回傳網頁狀態碼
 	print(e.code)
    # 顯示網頁表頭
 	print(e.headers)
