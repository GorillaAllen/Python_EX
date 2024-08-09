from matplotlib import pyplot as plt

age_group = ["under 18","19~25","26~30","31~35","36~40"]
age = [1000,2500,16514,2100,9874] 

plt.pie(age, labels = age_group,
# autopct = "%d%%", # put percentage label on the pie, no decimal
autopct = "%.2f%%", # put percentage label on the pie, 2 decimals
colors = ["#ef51a0","#62c451","#0547ab","#020ee4","#9a8bc1"], #set colors

        )

plt.show
