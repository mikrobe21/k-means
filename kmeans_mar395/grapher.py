import numpy as np
import pylab as pl
from numpy import *
import sys ## to get command line args

filepath = sys.argv[1]  #imports file
x, y, z = loadtxt(filepath, unpack=True)

x1=list()
y1=list()
x2=list()
y2=list()
x3=list()
y3=list()
x4=list()
y4=list()

i=0
while i<(len(z)):
	if (z[i]==1):
		x1.append(x[i])
		y1.append(y[i])
		i+=1
	elif(z[i]==2):
		x2.append(x[i])
		y2.append(y[i])
		i+=1
	elif(z[i]==3):
		x3.append(x[i])
		y3.append(y[i])
		i+=1
	else:
		x4.append(x[i])
		y4.append(y[i])
		i+=1

pl.plot(x1, y1, 'rs')
pl.plot(x2, y2, 'gp')
pl.plot(x3, y3, 'b*')
pl.plot(x4, y4, 'ch')
# show the plot on the screen
pl.show()