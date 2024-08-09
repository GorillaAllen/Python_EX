import xml.etree.ElementTree as ET

tree = ET.parse("hsinchuybike.xml")
print(tree)

root = tree.getroot()
print(root)


for son in root.findall("Data"): #root是根目錄的記憶體位置. son在for each裡表示根目錄下一層的標籤的記憶體位置
    month = son.find("所屬年月").text
    if month == "2021-7":
        root.remove(son)        
        
tree.write("ubikeSTA.xml", encoding = "utf8")
