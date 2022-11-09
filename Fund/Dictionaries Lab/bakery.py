items={}
food=input().split(" ")
for i in range(0, len(food), 2):
    key=food[i]
    value=food[i+1]
    items[key]=int(value)
print(items)