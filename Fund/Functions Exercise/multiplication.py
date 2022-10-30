def mult(a, b, c):
    seq=[a, b, c]
    if a==0 or b==0 or c==0:
        return "zero"
    neg=0
    for i in seq:
        if i<0:
            neg+=1
    if neg%2!=0:
        return "negative"
    else:
        return "positive"
    

num1=int(input())  
num2=int(input())   
num3=int(input())   
print(mult(num1, num2, num3))