import random
import math
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
def randomizePoints(point):
    point.x = random.randint(1,50)
    point.y = random.randint(1,50)
specialCase = False
with open('odcinek.txt','w') as fo:
    p = Point()
    q = Point()
    randomizePoints(p)
    randomizePoints(q)
    if (q.x - p.x) == 0: specialCase = True
    else:
        a = (q.y - p.y) / (q.x - p.x)
        b = p.y - a * p.x
    print("P = ({0},{1}), Q = ({2},{3})".format(p.x,p.y,q.x,q.
y))
    for row in range(1,51):
        for column in range(1,51):
            if specialCase == True:
                if ((p.y > q.y and row >= q.y and row <= p.y)
or (p.y < q.y and row >= p.y and row <= q.y)) and column == p.x: fo.write("*")
                else: fo.write(" ")
            else:
                if (column == p.x and row == p.y) or (column == q.x and row == q.y): fo.write("*")
                elif ((p.x > q.x and column > q.x and column < p.x) or (p.x < q.x and column < q.x and column > p.x)) and (math.isclose(row,(a * column + b),abs_tol=0.5)): fo.write("*")
                else: fo.write(" ")
        fo.write("\n")
fo.close()