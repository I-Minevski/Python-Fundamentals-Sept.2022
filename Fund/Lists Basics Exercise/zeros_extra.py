numbers=input().split(", ")
numbers=[int(x) for x in numbers]
zeros=[]
for i in range(len(numbers)-1, -1, -1):
    if numbers[i]==0:
        del numbers[i]
        zeros.append(0)
for zero in zeros:
    numbers.append(zero)
print(numbers)