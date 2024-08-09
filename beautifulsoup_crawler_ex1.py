from bs4 import BeautifulSoup

url = "Example.html"

with open(url, encoding="UTF-8") as file:
    soup = BeautifulSoup(file, "lxml")
    
tag = soup.div

print(tag.get_text("\n", strip=True))
