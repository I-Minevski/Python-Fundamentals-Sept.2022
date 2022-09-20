coffees=0
while True:
    word=input()
    if word=="END":
        break
    if word=="movie":
        coffees+=1
    elif word=="coding":
        coffees+=1
    elif word=="dog":
        coffees+=1
    elif word=="cat":
        coffees+=1
    elif word=="MOVIE":
        coffees+=2
    elif word=="CODING":
        coffees+=2
    elif word=="DOG":
        coffees+=2
    elif word=="CAT":
        coffees+=2
    else:
        continue
if coffees<=5:
    print(coffees)
else:
    print("You need extra sleep")
