sequence=input().split(" ")
sequence=[int(x) for x in sequence]
result=filter(lambda x: x%2==0, sequence)
print(list(result))