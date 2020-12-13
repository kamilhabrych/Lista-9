f = open("pierwsze.txt", "r")
read = f.read()
list_read = []
for item in read:
    print(item)
f.close()