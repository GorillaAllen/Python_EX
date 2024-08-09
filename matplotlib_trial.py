from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 50)
y = np.sin(x) + np.sin(x/3) + np.sin(x/4)/2

plt.rcParams["lines.linewidth"] = 1#調線寬

# manual = plt.rcParams.keys() 印出全部可調參數
# print(manual)

plt.grid(True)#顯示格線

# 設定中文
plt.rcParams["font.family"] = "Microsoft JhengHei"  # 微軟正黑體
# plt.rcParams['font.sans-serif'] = 'SimHei'        # mac電腦用
plt.rcParams["font.size"] = 14
plt.rcParams["axes.unicode_minus"] = False

#設定顏色與label
plt.plot(x,y,color="c", label = "trend") #cyan

#設定圖例
plt.legend()

#設定axis顯示範圍
# plt.xlim(-5,5)#x軸介於-5~5的圖
# plt.ylim(-2,2)#y軸介於-2~2的圖

#設定標題
plt.title("WOW")

#畫出來
plt.show()

