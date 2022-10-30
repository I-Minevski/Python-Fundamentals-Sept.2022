def add_num(arr, num):
    arr.append(num)


def remove_num(arr, num):
    if num in arr:
        arr.remove(num)


def replace_num(arr, num, rep):
    index=arr.index(num)
    arr[index]=rep


def collapse(arr, num):
    for i in range(len(arr)-1, -1, -1):
        if arr[i]<num:
            arr.remove(arr[i])


numbers=[int(num) for num in input().split(" ")]
while True:
    command=input()
    if command=="Finish":
        break
    com_list=command.split(" ")
    value=int(com_list[1])
    if "Add" in com_list:
        add_num(numbers, value)
    if "Remove" in com_list:
        remove_num(numbers, value)
    if "Replace" in com_list:
        replacement=int(com_list[2])
        replace_num(numbers, value, replacement)
    if "Collapse" in com_list:
        collapse(numbers, value)
print(' '.join(str(x) for x in numbers))