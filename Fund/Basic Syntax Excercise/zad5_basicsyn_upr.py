orders=int(input())
total=0
for i in range(orders):
    price=float(input())
    days=int(input())
    caps=int(input())
    cost=price*days*caps
    if price>=0.01 and price<=100 and days>=1 and days<=31 and caps>=1 and caps<=2000: 
        print(f"The price for the coffee is: ${cost:.2f}")
    else:
        continue
    total+=cost
print(f"Total: ${total:.2f}")