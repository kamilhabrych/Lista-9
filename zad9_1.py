import random

f = open('liczby.txt', "w")

for item in range(20):
    item = random.randint(1,100)
    f.write(str(item))
    f.write(" ")
f.close()