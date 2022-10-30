n=int(input())
numbers=[]
for i in range(n):
    num=int(input())
    numbers.append(num)
command=input()
final=[]
if command=="even":
    for i in numbers:
        if i%2==0:
            final.append(i)
if command=="odd":
    for i in numbers:
        if i%2!=0:
            final.append(i)
if command=="negative":
    for i in numbers:
        if i<0:
            final.append(i)
if command=="positive":
    for i in numbers:
        if i>=0:
            final.append(i)
print(final)