import math

def cartesian(x, y, z, t):
    distance1=(math.pow(x, 2) + math.pow(y, 2))
    distance2=(math.pow(z, 2) + math.pow(t, 2))
    if distance1<distance2:
        print(f"({math.floor(x)}, {math.floor(y)})")
    elif distance2<distance1:
        print(f"({math.floor(z)}, {math.floor(t)})")
    else:
        print(f"({math.floor(x)}, {math.floor(y)})")
        
        
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
cartesian(x1, y1, x2, y2)