operator=input()
num1=int(input())
num2=int(input())
def calculus(a, b, op):
    result=None
    if op=="add":
        result=a+b
    if op=="subtract":
        result=a-b
    if op=="multiply":
        result=a*b
    if op=="divide":
        result=a//b
    return result
print(calculus(num1, num2, operator))