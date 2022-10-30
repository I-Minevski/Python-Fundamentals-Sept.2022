def collect(arr, title):
    if title not in arr:
        arr.append(title)
    return arr


def drop(arr, title):
    if title in arr:
        arr.remove(title)
    return arr


def combine(arr, title):
    items=title.split(":")
    if items[0] in arr:
        index=arr.index(items[0])
        arr.insert(index+1, items[1])
    return arr


def renew(arr, title):
    if title in arr:
        renewing=arr[arr.index(title)]
        arr.remove(title)
        arr.append(renewing)
    return arr


inventory=input().split(", ")
while True:
    command=input()
    if command=="Craft!":
        break
    com_list=command.split(" - ")
    action=com_list[0]
    item=com_list[1]
    if action=="Collect":
        collect(inventory, item)
    if action=="Drop":
        drop(inventory, item)
    if action=="Combine Items":
        combine(inventory, item)
    if action=="Renew":
        renew(inventory, item)
print(', '.join(x for x in inventory))