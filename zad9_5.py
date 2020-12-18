import math
def roundCeil(x):
    return int(math.ceil(x/100))*100

with open('pierwsze.txt', 'r') as f1:
    for s in f1: 
        pass
    l = s.split(' ')
    l.pop()
    last = l.pop()
    f1.close()

with open('pierwsze.txt', 'a') as f2:
    y = roundCeil(int(last))
    x = y + 101
    f2.write("\n")
    for i in range(y,x):
        for j in range(2,i):
            if (i % j) == 0: 
                break
        else: 
            f2.write(str(i) + " ")
    f2.close()