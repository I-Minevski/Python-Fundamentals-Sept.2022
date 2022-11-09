from collections import OrderedDict
import operator

kin = {}
while True:
    info = input()
    if info == "Once upon a time":
        break
    name, hat_color, physics = info.split(" <:> ")
    physics = int(physics)
    if hat_color not in kin.keys():
        kin[hat_color] = {}
    if name not in kin[hat_color].keys():
        kin[hat_color][name] = physics
    if kin[hat_color][name] < physics:
        kin[hat_color][name] = physics

dwarf_attributes = {}
index = 0
for (color, dwarves) in kin.items():
    count = len(dwarves)
    for (name, physics) in dwarves.items():
        dwarf_attributes[str(index)] = {"color":color, "dwarves":count, "physics":physics, "name":name}
        index+=1
sorted_kin = (sorted(dwarf_attributes, key=lambda x: (dwarf_attributes[x]["physics"], dwarf_attributes[x]["dwarves"]), reverse=True))

for i in sorted_kin:
    print(f"({dwarf_attributes[i]['color']}) {dwarf_attributes[i]['name']} <-> {dwarf_attributes[i]['physics']}")
