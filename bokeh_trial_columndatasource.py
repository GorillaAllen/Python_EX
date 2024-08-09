from bokeh.plotting import figure, show
import pandas as pd
from math import pi
from bokeh.models import ColumnDataSource

data1 = {"x": [1,2,3,4],
         "y": [5,6,7,8]}

source = ColumnDataSource(data = data1)

p = figure()
