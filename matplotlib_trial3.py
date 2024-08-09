from matplotlib import pyplot as plt
import numpy as np

# x = np.linspace(-2*np.pi, 2*np.pi, 50)
# y = np.sin(x) + np.sin(x/3) + np.sin(x/4)/2

x1 = ["model A", "model B","model C","model D","model E"]
y1 = [500,600,1100,1600,2000]

x2 = ["model A", "model B","model C","model D","model E"]
y2 = [200,700,800,1600,2000]

x3 = ["model A", "model B","model C","model D","model E"]
y3 = [500,600,1500,1600,1100]

x4 = ["model A", "model B","model C","model D","model E"]
y4 = [400,600,1100,800,1000]

plt.rcParams["lines.linewidth"] = 1 #調線寬


#設定畫布
# plt.figure(figsize=(8,8)) #畫布大小

plt.grid(True)#顯示格線

# manual = plt.rcParams.keys() 印出全部可調參數
# print(manual)

# 設定中文
# plt.rcParams["font.family"] = "Microsoft JhengHei"  # 微軟正黑體
# # plt.rcParams['font.sans-serif'] = 'SimHei'        # mac電腦用
# plt.rcParams["font.size"] = 14
# plt.rcParams["axes.unicode_minus"] = False

#讓一張圖塞進多圖表
fig,ax = plt.subplots(2,2)
ax[0][0].plot(x1,y1)
ax[0][1].plot(x2,y2)
ax[1][0].plot(x3,y3)
ax[1][1].plot(x4,y4)
#設定各子圖間距
plt.subplots_adjust(hspace=0.3, wspace=0.5)


#設定顏色與label #marker設定線上的點
# plt.plot(x,y,color="c", label = "trend", marker = "o") #cyan

#設定圖例
# plt.legend()
# plt.legend(bbox_to_anchor=(1,1)) #讓圖例在外面

#讓值顯示在marker上
# for i, value in enumerate(y):
    # plt.text(i, value, value, ha="center", va = "bottom", fontsize = 15)



#設定axis顯示範圍
# plt.xlim(-5,5)#x軸介於-5~5的圖
# plt.ylim(0,2500)#y軸介於-2~2的圖


#畫出來
plt.show()

