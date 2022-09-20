import math
number=float(input())
if abs(number)<1 and number!=0:
    print("small", end=' ')
elif abs(number)>1000000:
    print("large", end=' ')
if number==0:
    print("zero")
if number>0:
    print("positive")
if number<0:
    print("negative")