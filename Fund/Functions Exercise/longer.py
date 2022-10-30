import math

def coord(a, b, c, d):
    dist=math.pow((a-c), 2) + math.pow((b-d), 2)
    return dist

x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
x3=float(input())
y3=float(input())
x4=float(input())
y4=float(input())
distance1=coord(x1, y1, x2, y2)
distance2=coord(x3, y3, x4, y4)
if distance1>distance2 or distance1==distance2:
    print((f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})"))
else:
    print((f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})"))