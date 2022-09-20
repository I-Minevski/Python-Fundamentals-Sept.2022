budget=int(input())
while True:
    product=input()
    if product=="End":
        print("You bought everything needed.")
        break
    budget-=int(product)
    if budget<0:
        print("You went in overdraft!")
        break
    