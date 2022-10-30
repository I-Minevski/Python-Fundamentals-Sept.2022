n=int(input())
for i in range(1, n+1):
    special=False
    j=i
    sum=0
    while j>0:
        sum+=j%10
        j//=10
    if sum==5 or sum==7 or sum==11:
        special=True
    print(f"{i} -> {special}")