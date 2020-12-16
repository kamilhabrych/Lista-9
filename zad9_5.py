import math
def roundUp(x):
    return int(math.ceil(x/100))*100

with open('pierwsze.txt', 'r') as f1:
    for s in f1: 
        pass
    s = s.replace(' ', 'x')
    l = s.split('x')
    l.pop()
    last_digit = l.pop()
    f1.close()

with open('pierwsze.txt', 'a') as f2:
    n = roundUp(int(last_digit))
    m = n + 101
    f2.write("\n")
    for i in range(n,m):
        for j in range(2,i):
            if (i % j) == 0: 
                break
        else: 
            f2.write(str(i) + " ")
    f2.close()