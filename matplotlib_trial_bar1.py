from matplotlib import pyplot as plt
import numpy as np

x = {"科目":["國文","英文","數學"]}
y = {"A的分數":[80,70,60],
     "B的分數":[20,30,20]}

# x = np.arange(len(x["科目"]))
# width = 0.3

# 設定中文
plt.rcParams["font.family"] = "Microsoft JhengHei"  # 微軟正黑體
# plt.rcParams['font.sans-serif'] = 'SimHei'        # mac電腦用
plt.rcParams["font.size"] = 14
plt.rcParams["axes.unicode_minus"] = False

#設定畫布, 1*row, 2*colomn. 一張畫布兩張圖
fig, ax = plt.subplots(1,2, figsize = (9,3))

bar1 = ax[0].bar(x["科目"], y["A的分數"], width = 0.3)
ax[0].set(ylabel="分數", title ="A同學", ylim = (0,100))
ax[0].bar_label(bar1) #設定bar資料標籤

bar2 = ax[1].bar(x["科目"], y["B的分數"], width = 0.3)
ax[1].set(title ="B同學", ylim = (0,100))
ax[1].bar_label(bar2) #設定bar資料標籤


plt.show
