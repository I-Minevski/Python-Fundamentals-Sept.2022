import sys
def smallest(a):
    tiny=sys.maxsize
    for i in range(a):
        number=int(input())
        if number<tiny:
            tiny=number
    return tiny

print(smallest(3))
