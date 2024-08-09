from bokeh.plotting import figure, show
import pandas as pd
from math import pi
from bokeh.transform import cumsum

# 設定資料
x = y = 0
radius = 0.7

data = {'United States': 157,
        'United Kingdom': 93,
        'Japan': 89,
        'China': 63,
        'Germany': 44,
        'India': 42,
        'Italy': 40,
        'Australia': 35,
        'Brazil': 32,
        'France': 31,
        'Taiwan': 31,
        'Spain': 29}

# 將資料做成Series
df = pd.Series(data).reset_index(name="value").rename(columns={"index":"country"})
# 計算各個圓餅的面積
df["area"] = df["value"] / df["value"].sum() * 2 * pi
df["color"] = ["#FF3333","#FF7744","#FFCC22","#CCFF33",
                 "#33FF33","#33FFAA","#33FFFF","#5599FF",
                 "#7744FF","#B94FFF","#E93EFF","#FF3EFF"]

# 設定畫布
p = figure(x_range = (-0.8, 1.5),  # 設定x軸的範圍為-0.8~1.5之間
           tooltips = "@country: @value")  # 設定tooltips

# 繪製圓餅圖
p.wedge(x, y, radius, 
        start_angle = cumsum("area", include_zero=True),  # 圓餅的起始角度
        end_angle = cumsum("area"),  # 圓餅的結束角度
        # source = df,  # 資料來源
        fill_color = "color",  # 圓餅顏色
        line_color = "#FFFFFF",  # 線條顏色
        legend_field = "country")   # 圖例

# 顯示圖表
show(p)
