encrypted=input()
num=[char for char in encrypted if '0'<=char<='9']
encrypted=''.join(char for char in encrypted if not '0'<=char<='9')
keep=[int(num[i]) for i in range(len(num)) if i %2==0]
skip=[int(num[i]) for i in range(len(num)) if not i %2==0]
result=""
for i in range(len(keep)):
    result+=encrypted[:keep[i]]
    removal=encrypted[:(keep[i]+skip[i])]
    encrypted=encrypted.split(removal)
    encrypted=''.join(x for x in encrypted)
print(result)