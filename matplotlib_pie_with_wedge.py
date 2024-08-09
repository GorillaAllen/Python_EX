from matplotlib import pyplot as plt

age_group = ["under 18","19~25","26~30","31~35","36~40"]
age = [1000,2500,16514,2100,9874] 

# 設定中文
plt.rcParams["font.family"] = "Microsoft JhengHei"  # 微軟正黑體
# plt.rcParams['font.sans-serif'] = 'SimHei'        # mac電腦用
plt.rcParams["font.size"] = 14
plt.rcParams["axes.unicode_minus"] = False

plt.pie(age, labels = age_group,
# autopct = "%d%%", # put percentage label on the pie, no decimal
autopct = "%.2f%%", # put percentage label on the pie, 2 decimals
colors = ["#ef51a0","#62c451","#0547ab","#020ee4","#9a8bc1"], #set colors
radius = 1.4, #set size. default is 1
pctdistance=0.7, # percentage's distance from center
#set a wedge
wedgeprops={"linewidth":3,
            "edgecolor":"w",
            "width":0.8}
        )

plt.title("TTTTT")
plt.show
