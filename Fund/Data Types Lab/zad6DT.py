year=int(input())
while True:
    year+=1
    dali=True
    a=year
    unique=[]
    while a>0:
        figure=a%10
        if figure not in unique:
            unique.append(figure)
        else:
            dali=False
            break
        a//=10
    if dali==True:
        print(year)
        break
