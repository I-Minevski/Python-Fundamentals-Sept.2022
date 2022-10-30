n=int(input())
word=input()
strings=[]
for i in range(n):
    new_string=input()
    strings.append(new_string)
print(strings)
for i in range(len(strings)-1, -1, -1):
    if word not in strings[i]:
        strings.remove(strings[i])
print(strings)