number=int(input())
digits=list()
br=0
while number>0:
    a=number%10
    number=number//10
    digits.append(a)
    br+=1
for i in range(br):
    for j in range(br-1):
        if digits[j]<digits[j+1]:
            swap=digits[j]
            digits[j]=digits[j+1]
            digits[j+1]=swap
for i in digits:
    print(i, end='')
