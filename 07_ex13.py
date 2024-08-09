import pandas as pd
x = {"姓名":["小林","小黃","小陳","小美"],
 "國語":[75,91,71,69],
 "數學":[62,53,88,53],
 "英文":[85,56,51,87],
 "自然":[73,63,69,74],
 "社會":[60,65,87,70]}

y = pd.DataFrame(x)
# print(y)
# print(y[:][2:4])

print(y[:][2:4].sort_values("自然",ascending = False),"\n")

print(y[["姓名","自然"]].sort_values("自然",ascending = False),"\n")

print(y[:][1:2])

# print(x["國語"][1])
# print(x["數學"][1])
# print(x["英文"][1])
# print(x["自然"][1])
# print(x["社會"][1])
