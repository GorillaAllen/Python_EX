import requests

url = "https://cuiqingcai.com/indea.html"

response = requests.get(url)
# print(type(response))

if response.status_code == 200: # requests.codes.ok
    print("Successfully aquires webpage content")
    print("url of the page is ",response.url)
    print("headers are: ", response.headers)
    print("cookie: ", response.cookies)
else:
    print("fail to get website contend")

# try:
#     response = requests.get(url)
# except:
#     print("fail")
#     #要加上error事件比較有用
