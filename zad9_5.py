import math
def roundUp(x):
    return int(math.ceil(x/100))*100

with open('pierwsze.txt', 'r') as fo:
    for s in fo: 
        pass
    s = s.replace(' ', 'x')
    l = s.split('x')
    l.pop()
    last_digit = l.pop()
    fo.close()

with open('pierwsze.txt', 'a') as fa:
    n = roundUp(int(last_digit))
    m = n + 101
    fa.write("\n")
    
    for i in range(n,m):
        for j in range(2,i):
            if (i % j) == 0: break
        else: fa.write(str(i) + " ")
    fa.close()