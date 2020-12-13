import random

f = open('file2.txt', 'w')

char = [' ', '*']

for item in range(50):
    for item in range(50):
        random_char = random.choice(char)
        f.write(random_char)
    f.write("\n")
f.close()