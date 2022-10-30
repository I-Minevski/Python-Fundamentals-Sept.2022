seq=input()
amounts=seq.split(", ")
amounts=[int(x) for x in amounts]
count=int(input())
beggars=[]
for i in range(count):
    beggars.append(0)
j=0
for i in range(len(amounts)):
    if j>=count:
        j=0
    beggars[j]+=amounts[i]
    j+=1
print(beggars)