#CS4315
#Spring 2017
#FEB 25
#Michael Robertson

import math
from numpy import *
import sys ## to get command line args
import copy

class Point():
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def getX(self):
		return int(self.x)
	
	def getY(self):
		return int(self.y)
	
	def distance(self, other):
		dx = self.x - other.x
		dy = self.y - other.y
		return math.sqrt(dx**2 + dy**2)
		#return math.hypot(dx, dy) #same as above
	
	def myCentroid(self, myCentroid=0):
		self.myCentroid = myCentroid	
		
	def getMyCentroid(self):
		return self.myCentroid 

requiredCentroids = int(sys.argv[1]) # saves number of requested centroids
filepath = sys.argv[2]  #imports file
	    	
#read in a file here / add x/y coords to points
xArray, yArray = loadtxt(filepath, unpack=True) #DataIn is a 2D array with our values

#create array of points   
pointList = [] 
i = 0
while i < (len(xArray)): #populate the list with Points
	pointList.append(Point(xArray[i], yArray[i]))
	i+=1
	
centroidList = []

n = 0
while n < (requiredCentroids): 
	rand = random.randint(0, len(pointList))
	centroidList.append(Point(xArray[rand], yArray[rand]))
	n+=1

##MAIN LOOP###

distanceSum = 100
while (distanceSum > 0):	
	j = 0
	while j < (len(xArray)): ##assign points to closest centroid
	
		distanceList = []

		l=0
		while l < (requiredCentroids): ##good
			distanceList.append(pointList[j].distance(centroidList[l]))
			l+=1
		
		pointList[j].myCentroid = (1 + distanceList.index(min(distanceList)))
		j+=1
	
	oldCentroidList = centroidList ##experiment
	centroidList = []
	
	y=1
	while y <= (requiredCentroids):
		sumX = 0
		sumY = 0
		counter = 0
		z=0
		while z < (len(xArray)):
			
			if (int(pointList[z].getMyCentroid()) == y):
				sumX += int(pointList[z].getX())
				sumY += int(pointList[z].getY())
				counter += 1	
			z+=1

		if (counter > 0):	
			avgX = int(sumX/counter)
			avgY = int(sumY/counter)
			centroidList.append(Point(avgX, avgY))
		else:
			centroidList.append(Point(0, 0))
		y+=1
		
	q = 0	
	distanceSum = 0
	while q < (requiredCentroids):
		distanceSum += oldCentroidList[q].distance(centroidList[q])
		q+=1	

#create text files after processing data
text_file = open("output.txt", "w")

k = 0
while k < (len(pointList)):
	#print pointList[k].getX()
	text_file.write(str(pointList[k].getX()))
	text_file.write(" ")
	text_file.write(str(pointList[k].getY()))
	text_file.write(" ")
	text_file.write(str(pointList[k].getMyCentroid()))
	text_file.write("\n")
	k+=1

text_file.close()	