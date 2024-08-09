from bokeh.plotting import figure, show
import numpy as np

#!未完成

x = np.linspace(0,np.pi*2,20)
y = np.sin(x)

#set a frame to put everything in it. A must
p = figure(
    # x_range = x,
    # width = 500, #frame width
    # height=500, #frameheight
    title = "SIN(X)",
    x_axis_label = "X",
    y_axis_label = "Sin(X)",
    background_fill_color = "#ffffff"
    )

#draw the bar fig
p.vbar(x,y, width=0.4)

# No show x grid
p.xgrid.grid_line_color = None
#set y axis bottom as bar fig needs no to show what's below buttom
p.y_range.start = -1

show(p)
