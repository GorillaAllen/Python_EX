from bokeh.plotting import figure, show
import numpy as np

x = np.linspace(0,np.pi*2)
y = np.sin(x)

#set a frame to put everything in it. A must
p = figure(width = 500, #frame width
    height=500, #frameheight
    title = "SIN(X)",
    x_axis_label = "X",
    y_axis_label = "Sin(X)",
    background_fill_color = "#033004"
    )

#draw the line
p.line(x,y,
       line_width = 1.5
       )

#default setting of this statement is to open a web browser to shoe figure
show(p)

 
