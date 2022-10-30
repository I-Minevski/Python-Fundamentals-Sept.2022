def tri(a):
    sequence=[1, 1, 2]
    add=sum(sequence)
    for i in range(3, a):
        sequence.append(add)
        add=sequence[i]+sequence[i-1]+sequence[i-2]
    return sequence
    

count=int(input())
tri_list=tri(count)
if count==1:
    tri_list=[1]
elif count==2:
    tri_list=[1, 1]
elif count==3:
    tri_list=[1, 1, 2]
for i in tri_list:
    print(i, end=" ")