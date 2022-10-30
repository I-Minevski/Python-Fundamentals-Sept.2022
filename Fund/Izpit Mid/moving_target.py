def shoot(arr, i, power):
    if i in range(len(arr)):
        arr[i]-=power
        if arr[i]<=0:
            arr.remove(arr[i])
        

def add_tar(arr, i, value):
    if i in range(len(arr)):
        arr.insert(i, value)
    else:
        print("Invalid placement!")


def strike(arr, i, radius):
    indices=[x for x in range(i-radius, i+radius+1)]
    removed=[]
    is_valid=True
    for x in indices:
        if x not in range(len(arr)):
            is_valid=False
            break
    if is_valid==False:
        print("Strike missed!")
    else:
        for x in indices:
            removed.append(arr[x])
        for x in removed:
            arr.remove(x)
            

targets=[int(tar) for tar in input().split(" ")]
while True:
    command=input()
    if command=="End":
        break
    com_list=command.split(" ")
    index=int(com_list[1])
    whatever=int(com_list[2])
    if "Shoot" in com_list:
        shoot(targets, index, whatever)
    if "Add" in com_list:
        add_tar(targets, index, whatever)
    if "Strike" in com_list:
        strike(targets, index, whatever)
print('|'.join(str(x) for x in targets))