numbers=input().split(" ")
numbers=[float(x) for x in numbers]
absolut=[]
for i in range(len(numbers)):
    absolut.append(abs(numbers[i]))
print(absolut)