divisor=int(input())
boundary=int(input())
for i in range(boundary+1):
    if i>0 and i%divisor==0:
        n=i
print(n)