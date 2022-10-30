items=input().split("|")
budget=float(input())
b=budget
is_enough=False
prices=[]
for i in range(len(items)):
    product=items[i].split("->")
    type=product[0]
    price=float(product[1])
    if type=="Clothes":
        if price>50.00:
            continue
    elif type=="Shoes":
        if price>35.00:
            continue
    elif type=="Accessories":
        if price>20.50:
            continue
    if budget-price<0:
        continue
    else:
        budget-=price
        prices.append(price)
for i in range(len(prices)):
    print(f"{prices[i]*140*0.01:.2f}", end=" ")
    budget+=140*0.01*prices[i]
print(f"\nProfit: {budget-b:.2f}")
if budget>=150:
    print("Hello, France!")
else:
    print("Not enough money.")