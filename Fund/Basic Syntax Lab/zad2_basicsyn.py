a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    largest=a
if b>c and b>a:
    largest=b
if c>b and c>a:
    largest=c
print(largest)