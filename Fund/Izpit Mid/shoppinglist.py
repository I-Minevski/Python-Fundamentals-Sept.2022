def urgent(arr, name):
    if name not in arr:
        arr.insert(0, name)
    return arr


def unnecessary(arr, name):
    if name in arr:
        arr.remove(name)
    return arr


def correct(arr, old, new):
    if old in arr:
        index=arr.index(old)
        arr[index]=new
    return arr

def rearrange(arr, name):
    if name in arr:
        arr.remove(name)
        arr.append(name)
    return arr


groceries=input().split("!")
while True:
    command=input()
    if command=="Go Shopping!":
        break
    com_list=command.split(" ")
    item=com_list[1]
    if "Urgent" in com_list:
        urgent(groceries, item)
    if "Unnecessary" in com_list:
        unnecessary(groceries, item)
    if "Correct" in com_list:
        new_item=com_list[2]
        correct(groceries, item, new_item)
    if "Rearrange" in com_list:
        rearrange(groceries, item)
print(', '.join(x for x in groceries))