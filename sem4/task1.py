from random import gauss
from matplotlib import pyplot as plt
import numpy as np
xlist = []
ylist = []
for i in range(3, 50):
    xlist.append(i)
    j = gauss(3 * i, 2)
    ylist.append(j)
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)
x = [3, 50]
y = np.interp(x, xlist, ylist)
ax1.scatter(xlist, ylist, marker = '.', color = 'k')
ax1.errorbar(xlist, ylist, yerr = 2, xerr = 0.3, color =  'k', linestyle = 'None')
ax1.plot(x, y, 'r')
ax1.grid()
plt.show()




    

    

