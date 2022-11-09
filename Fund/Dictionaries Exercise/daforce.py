def initiation(ordo, path, memb):
    if path not in ordo.keys():
        ordo[path]=[]
    is_user=False
    for value in ordo.values():
        if memb in value:
            is_user=True
    if is_user==False:
        ordo[path].append(memb)


def fall(ordo, memb, path):
    for key, value in ordo.items():
        if memb in value:
            del ordo[key][value.index(memb)]
    if path not in ordo.keys():
        ordo[path]=[memb]
    else:
        ordo[path].append(memb)    
    print(f"{memb} joins the {path} side!")

order={}
while True:
    command=input()
    if command=="Lumpawaroo":
        break
    if "|" in command:
        com=command.split(" | ")
        side, user = com
        initiation(order, side, user)
    if ">" in command:
        com=command.split(" -> ")
        user, side = com
        fall(order, user, side)
for (key, value) in order.items():
    if len(order[key])>0:
        print(f"Side: {key}, Members: {len(order[key])}")
        for member in order[key]:
            print(f"! {member}")