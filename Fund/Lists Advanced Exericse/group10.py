def grouping(arr, b):
    group=[]
    for i in range(len(arr)-1, -1, -1):
        if arr[i]<=b:
            group.append(arr[i])
            del arr[i]
    return group


seq=[int(number) for number in input().split(", ")]
boundary=10
maxel=max(seq)
if maxel%10!=0:
    maxel//=10
    maxel*=10
while boundary<=maxel:
    print(f"Group of {boundary}'s: {list(reversed(grouping(seq, boundary)))}")
    boundary+=10
if len(seq)>0:
    print(f"Group of {boundary}'s: {(seq)}")