import random
import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def randomizePoints(point):
    point.x = random.randint(1,50)
    point.y = random.randint(1,50)
def printPattern(radius,point):
    for i in range((2 * radius)+1):
        for j in range((2 * radius)+1):
            dist = math.sqrt((i - radius) * (i - radius) + (j - radius) * (j - radius))
            if (dist > radius - 0.5 and dist < radius + 0.5):
                listOfPoints.append(Point(point.y+radius-j,point.x+radius-i))
notFound = True
listOfPoints = []
p = Point(0,0)
randomizePoints(p)

while 1:
    radius = random.randint(1,50)
    if p.x+radius <= 50 and p.x - radius >= 1 and p.y+radius <= 50 and p.y-radius >= 1:
        break
printPattern(radius,p)

with open('okrag.txt','w') as f1:
    for row in range(1,51):
        for column in range(1,51):
            notFound = True
            for obj in listOfPoints:
                if (column == obj.x and row == obj.y):
                    f1.write("*")
                    notFound = False
            if notFound == True: 
                f1.write(" ")
        f1.write("\n")
    f1.close()