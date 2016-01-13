import baseStatistics as stat
import numpy
import physics
import math
import matplotlib.pyplot as plt
import baseMetrics as b

#print(stat.distributionSorter([3,6,8,9,1,3,54,6,2,56,2,3,1,55,77,32,2,4,6],[1,2,3,4,5,6,7,8,9,10]))

y = []
x = []
for i in range(600):
    x.append(i/30)
    y.append( math.sin(x[i]))


z = b.slidingGradient(x,y,3*math.pi,0,1)


plt.figure()
plt.plot(x,y)


plt.plot(x[0:len(x)-1],(z),color='g')
plt.plot(x,[0] * len(x),color='y')
plt.plot([math.pi/2] * len(z),z,color='y')
plt.show()