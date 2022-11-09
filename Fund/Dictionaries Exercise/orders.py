stock={}
while True:
    product=input().split(" ")
    if product[0]=="buy":
        break
    item=product[0]
    price=float(product[1])
    quantity=int(product[2])
    if item not in stock.keys():
        stock[item]=[]
        stock[item].append(price)
        stock[item].append(0)
    stock[item][0]=price
    stock[item][1]+=quantity
for (key, value) in stock.items():
    print(f"{key} -> {value[0]*value[1]:.2f}")