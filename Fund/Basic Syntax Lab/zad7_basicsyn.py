num=int(input())
for i in range(1, num+1):
    j=i
    while j>0:
        print("*", end='')
        j-=1
    print("")
for i in range(num-1, 0, -1):
    j=i
    while j>0:
        print("*", end='')
        j-=1
    print("")
