food=float(input())
hay=float(input())
cover=float(input())
pig_weight=float(input())
day=1
is_ok=True
while day<=30:
    food-=0.3
    if day%2==0:
        hay-=5*0.01*food
    if day%3==0:
        cover-=(pig_weight/3)
    if food<0 or hay<0 or cover<0:
        print("Merry must go to the pet store!")
        is_ok=False
        break
    day+=1
if is_ok==True:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")