import numpy as np

#numpy array只收list, 所以先做list
a = []

for i in range(0,51,10): #聰明但難懂
    for j in range(i,i+6):
        a.append(j)
    
#簡單粗暴
# for i in range(0,6):
#     a.append(i)
# for i in range(10,16):
#     a.append(i)
# for i in range(20,26):
#     a.append(i)
# for i in range(30,36):
#     a.append(i)
# for i in range(40,46):
#     a.append(i)
# for i in range(50,56):
#     a.append(i)
    
# print(a)

k = np.array(a).reshape(6,6) #轉二維
# print(k)

print(k[np.ix_([0,5],[0,5])])
print(k[2:4,3:5])
print("每一排總和")
for i in range(0,6):
    print("第%d排:%d" %(i+1, k[i].sum()))
