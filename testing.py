import baseStatistics as stat
import numpy
import physics
import math
import matplotlib.pyplot as plt
import baseMetrics as b
from patient import patient
from operator import itemgetter

#print(stat.distributionSorter([3,6,8,9,1,3,54,6,2,56,2,3,1,55,77,32,2,4,6],[1,2,3,4,5,6,7,8,9,10]))


"""
y = []
x = []
for i in range(600):
    x.append(i/30)
    y.append( math.sin(x[i]))


z = b.slidingGradient(x,y,3*math.pi,0,1)
#def __init__(self, name, x, y, time, distance, events):
#peti = patient('peti',0,0,0,0,[['success',1],['fail',2],['nnyenye',3]])
csicsoka = []
csicsoka.append([1,2,3])
csicsoka.append([4,5])
csicsoka.append([6])
baboka =[]
baboka.append(csicsoka)
#csicsoka = [[1,2,3],[4,5],[6]]

print(baboka[0])

plt.figure()
plt.plot(x,y)


plt.plot(x[0:len(x)-1],(z),color='g')
plt.plot(x,[0] * len(x),color='y')
plt.plot([math.pi/2] * len(z),z,color='y')
plt.show()

"""


a = [1,2,3,4,5, 6, 7, 8, 9, 11, 100, 555, 777, 888, 999]
keresendo = 555.6
pair = min(enumerate(abs(numpy.subtract(a,[keresendo]*len(a)))), key=itemgetter(1))
a=[]
a=a+[5]
a.append(4)
print(a)


