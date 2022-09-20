word=input()
br=0
indeces=list()
for i in word:
    if i>='A' and i<="Z":
        indeces.append(br)
    br+=1
print(indeces)