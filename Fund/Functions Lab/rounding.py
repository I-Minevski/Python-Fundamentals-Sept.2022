numbers=input().split(" ")
numbers=[float(x) for x in numbers]
rounded=[]
for i in range(len(numbers)):
    rounded.append(round(numbers[i]))
print(rounded)