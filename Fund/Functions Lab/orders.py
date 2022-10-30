item=input()
amount=int(input())
def total(a, b):
    sum=0
    if a=="coffee":
        sum=b*1.5
    if a=="water":
        sum=b*1
    if a=="coke":
        sum=b*1.4
    if a=="snacks":
        sum=b*2
    return sum
final=total(item, amount)
print(f"{final:.2f}")