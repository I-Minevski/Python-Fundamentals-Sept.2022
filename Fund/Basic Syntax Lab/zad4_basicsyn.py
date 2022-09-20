n=int(input())
AreAllEven=True
while n!=0:
    number=int(input())
    if number%2!=0:
        AreAllEven=False
        print(f"{number} is odd!")
        break
    n-=1
if AreAllEven==True:
    print(f"All numbers are even.")