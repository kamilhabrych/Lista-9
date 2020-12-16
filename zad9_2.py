f = open("liczby.txt", "r")

l = []

space = ""

while True:
    s = f.read(1)
    if s == "":
        break
    if s.isnumeric():
        space += str(s)
    elif s.isspace():
        l.append(int(space))
        space = ""

print(l)

f.close()