import pandas as pd
x = pd.DataFrame({"key":["a","b","c","d"],
     "value":           [ 1,  2,  3,  4]})
y = pd.DataFrame({"key":["b","c","d","e"],
     "value":           [ 2,  3,  4,  5]})

# print(x)
# print(y)
# print(pd.concat([x,y],axis=1)) #axis = 1表示"新增colume"
                               #axis = 0表示"新增row"

# z = pd.merge(x,y, how = "inner")#inner取交集.欄位名&值都要一樣才算是有交集
# print(z)                        

m = pd.merge(x,y, how = "outer")#outer取聯集.欄位名&值只要其中一樣不同就算是在聯集裡
print(m) 
