import random
import math

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

def randomPoints(point):
    point.x = random.randint(1,50)
    point.y = random.randint(1,50)

equal = False

with open('odcinek.txt','w') as f1:

    p = Point()
    q = Point()
    randomPoints(p)
    randomPoints(q)

    if (q.x - p.x) == 0: 
        equal = True
    else:
        a = (q.y - p.y) / (q.x - p.x)
        b = p.y - a * p.x

    print("P = ({0},{1})".format(p.x,p.y))
    print("Q = ({0},{1})".format(q.x,q.y))

    for row in range(1,50+1):
        for column in range(1,50+1):
            if equal == True:
                if ((p.y > q.y and row >= q.y and row <= p.y) or (p.y < q.y and row >= p.y and row <= q.y)) and column == p.x: 
                    f1.write("*")
                else: 
                    f1.write(" ")
            else:
                if (column == p.x and row == p.y) or (column == q.x and row == q.y): 
                    f1.write("*")
                elif ((p.x > q.x and column > q.x and column < p.x) or (p.x < q.x and column < q.x and column > p.x)) and (math.isclose(row,(a * column + b),abs_tol=0.5)): 
                    f1.write("*")
                else: 
                    f1.write(" ")
        f1.write("\n")
f1.close()