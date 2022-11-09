items={}
food=input().split(" ")
for i in range(0, len(food), 2):
    key=food[i]
    value=food[i+1]
    items[key]=int(value)
inquire=input().split(" ")
for i in range(len(inquire)):
    if inquire[i] in items.keys():
        print(f"We have {items[inquire[i]]} of {inquire[i]} left")
    else:
        print(f"Sorry, we don't have {inquire[i]}")