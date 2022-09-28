budget=float(input())
price_flour=float(input())
price_egg=75*0.01*price_flour
price_milk=125*0.01*price_flour
eggs=made_total=0
while budget>0:
    loaf=price_egg+price_flour+25*0.01*price_milk
    budget-=loaf
    if budget<0:
        budget=budget+loaf
        break
    eggs+=3
    made_total+=1
    if made_total%3==0:
        eggs=eggs-(made_total-2)
print(f"You made {made_total} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.") 
