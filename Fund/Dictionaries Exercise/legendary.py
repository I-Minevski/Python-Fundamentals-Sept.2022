inventory={"shards" : 0, "fragments" : 0, "motes" : 0}
is_done=False
while True:
    stuff=[word.lower() for word in input().split(" ")]
    for i in range(0, len(stuff), 2):
        quantity=stuff[i]
        material=stuff[i+1]
        if material not in inventory.keys():
            inventory[material]=0
        inventory[material]+=int(quantity)
        if inventory["shards"]>=250:
            print("Shadowmourne obtained!")
            inventory["shards"]-=250
            is_done=True
            break
        if inventory["fragments"]>=250:
            print("Valanyr obtained!")
            inventory["fragments"]-=250
            is_done=True
            break
        if inventory["motes"]>=250:
            print("Dragonwrath obtained!")
            inventory["motes"]-=250
            is_done=True
            break
    if is_done==True:
        break
for (key, value) in inventory.items():
    print(f"{key}: {value}")