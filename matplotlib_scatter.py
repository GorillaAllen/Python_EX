from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1,21)
y = np.random.randint(1,100,20)
size = np.random.randint(1,100,20)*2

#scatter figure
plt.scatter(x,y, #data source
            color = "c", #dot color
            edgecolor = "y", #dot edge color
            s = size #dot size
            )


plt.show()
