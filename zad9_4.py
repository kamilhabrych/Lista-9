f = open('pierwsze.txt', 'w')

for item in range(2,100+1):
    for number in range(2,item):
        if item % number == 0:
            break
    else:
        f.write(str(item))
        f.write(" ")
 
f.close()