from matplotlib import pyplot as plt
import numpy as np

# x = np.linspace(-2*np.pi, 2*np.pi, 50)
# y = np.sin(x) + np.sin(x/3) + np.sin(x/4)/2

x = ["model A", "model B","model C","model D","model E"]
y = [500,600,1100,1600,2000]

plt.rcParams["lines.linewidth"] = 1 #調線寬


#設定畫布
plt.figure(figsize=(8,8)) #畫布大小

plt.grid(True)#顯示格線

# manual = plt.rcParams.keys() 印出全部可調參數
# print(manual)

# 設定中文
# plt.rcParams["font.family"] = "Microsoft JhengHei"  # 微軟正黑體
# # plt.rcParams['font.sans-serif'] = 'SimHei'        # mac電腦用
# plt.rcParams["font.size"] = 14
# plt.rcParams["axes.unicode_minus"] = False



#設定顏色與label #marker設定線上的點
plt.plot(x,y,color="c", label = "trend", marker = "o") #cyan

#設定圖例
plt.legend()
# plt.legend(bbox_to_anchor=(1,1)) #讓圖例在外面

#讓值顯示在marker上
for i, value in enumerate(y):
    plt.text(i, value, value, ha="center", va = "bottom", fontsize = 15)



#設定axis顯示範圍
# plt.xlim(-5,5)#x軸介於-5~5的圖
plt.ylim(0,2500)#y軸介於-2~2的圖


#畫出來
plt.show()

