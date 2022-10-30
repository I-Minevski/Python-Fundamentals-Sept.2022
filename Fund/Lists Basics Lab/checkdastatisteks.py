n=int(input())
pos=[]
neg=[]
for i in range(n):
    number=int(input())
    if number>=0:
        pos.append(number)
    else:
        neg.append(number)
print(pos)
print(neg)
print(f"Count of positives: {len(pos)}\nSum of negatives: {sum(neg)}")