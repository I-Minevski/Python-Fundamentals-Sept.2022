def percentage(a):
    if a!=100:
        print(f"{a}% [", end="")
        count=a/10
        points=10-count
        while count>0:
            print("%", end="")
            count-=1
        while points>0:
            print(".", end="")
            points-=1
        print("]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


num=int(input())
percentage(num)        