herd=list()
line=input()
index=0
for i in range(len(line)):
    if line[i]=="s":
        animal=line[i:i+5]
        herd.append(animal)
        index+=1
    elif line[i]=="w":
        animal=line[i:i+4]
        herd.append(animal)
        index+=1
br=0
for jivotno in range(index-1, -1, -1):
    br+=1
    if herd[index-1]=="wolf":
        print(f"Please go away and stop eating my sheep")
        break
    if herd[jivotno]=="wolf":
        print(f"Oi! Sheep number {br-1}! You are about to be eaten by a wolf!")