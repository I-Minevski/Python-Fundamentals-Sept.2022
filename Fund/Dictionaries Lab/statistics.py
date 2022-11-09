items={}
while True:
    command=input()
    if command=="statistics":
        break
    com_list=command.split(": ")
    key=com_list[0]
    value=com_list[1]
    if key not in items.keys():
        items[key]=int(value)
    else:
        items[key]+=int(value)
print("Products in stock:")
for i in items.keys():
    print(f"- {i}: {items[i]}")
print(f"Total Products: {len(items.keys())}")
print(f"Total Quantity: {sum(items.values())}")