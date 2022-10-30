happiness=input().split(" ")
happiness=list(map(int, happiness))
mul=int(input())
multiplied=list(map(lambda x: x*mul, happiness))
avrg=sum(multiplied)/len(multiplied)
happy=list(filter(lambda x: x>=avrg, multiplied))
if len(happy)>=len(multiplied)/2:
    print(f"Score: {len(happy)}/{len(multiplied)}. Employees are happy!")
else:
    print(f"Score: {len(happy)}/{len(multiplied)}. Employees are not happy!")