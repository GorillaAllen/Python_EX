import requests
import re
key = "DEF BCD CDE ABC XYZ"

url = "http://koeido-mak.com/TIgs_list.htm"

htmlfile = requests.get(url)

if htmlfile.status_code == requests.codes.ok:
    pattern = input("Les Paul")
    
name = re.findall(pattern, htmlfile.text)

print(name)

# pattern1 = re.compile(r'^DEF\D{8}')
# rs1 = pattern1.findall(key)

# #ABC XYZ
# pattern2 = re.compile(r'ABC.XYZ')
# rs2 = pattern2.findall(key)

# #XY
# pattern3 = re.compile(r'XY')
# rs3 = pattern3.findall(key)

# print(rs1)
# print(rs2)
# print(rs3)