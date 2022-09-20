herd=list()
line=input()
for i in line:
    if i=='s':
        animal=line[i:i+5:]
        herd.append(animal)
    elif i=='w':
        animal=line[i:i+4:]
        herd.append(animal)
print(herd)