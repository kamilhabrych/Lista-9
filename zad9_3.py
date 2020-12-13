f = open('file.txt', 'w')

for item in range(50):
    for item in range(50):
        print(end="*")
        f.write("*")
    print()
    f.write("\n")

f.close()    