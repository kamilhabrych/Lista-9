import random
import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def randomPoints(point):
    point.x = random.randint(1,50)
    point.y = random.randint(1,50)

def printCircle(radius,point):
    for i in range((2 * radius)+1):
        for j in range((2 * radius)+1):
            x = math.sqrt((i - radius) * (i - radius) + (j - radius) * (j - radius))
            if (x > radius - 0.5 and x < radius + 0.5):
                Points.append(Point(point.y+radius-j,point.x+radius-i))

notFound = True
Points = []
p = Point(0,0)
randomPoints(p)

while True:
    radius = random.randint(1,50)

    if p.x + radius <= 50 and p.x - radius >= 1 and p.y + radius <= 50 and p.y - radius >= 1:
        break
    
printCircle(radius,p)

with open('circle.txt','w') as f1:
    for row in range(1,50+1):
        for column in range(1,50+1):
            notFound = True
            for i in Points:
                if (column == i.x and row == i.y):
                    f1.write("*")
                    notFound = False
            if notFound == True: 
                f1.write(" ")
        f1.write("\n")
    f1.close()