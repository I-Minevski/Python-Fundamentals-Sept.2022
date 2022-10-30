n=int(input())
capacity=int(input())
if n%capacity==0:
    print(n//capacity)
else:
    print(n//capacity+1)