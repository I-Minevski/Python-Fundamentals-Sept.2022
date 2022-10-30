targets=[int(number) for number in input().split(" ")]
shot=0
while True:
    index=input()
    if index=="End":
        break
    index=int(index)
    if index in range(len(targets)):
        current=targets[index]
        targets[index]=-1
        shot+=1
        for i in range(len(targets)):
            if targets[i]!=-1:
                if targets[i]<=current:
                    targets[i]+=current
                else:
                    targets[i]-=current
printing=" ".join(str(x) for x in targets)
print(f"Shot targets: {shot} -> {printing}")