class Dragon():

    def __init__(self, name, damage=45, health=250, armor=10):
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor

    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage

    def get_health(self):
        return self.health

    def get_armor(self):
        return self.armor


dragons_count = int(input())
army = {}
for i in range(dragons_count):
    dragon_info = input().split(" ")
    type, dragon_name, dmg, hlth, armr = dragon_info
    if type not in army.keys():
        army[type] = []
    if "null" not in dragon_info:
        dragon = Dragon(dragon_name, int(dmg), int(hlth), int(armr))
    else:
        if dmg == "null":
            dragon = Dragon(name=dragon_name, health=int(hlth), armor=int(armr))
        if hlth == "null":
            dragon = Dragon(name=dragon_name, damage=int(dmg), armor=int(armr))
        if armr == "null":
            dragon = Dragon(name=dragon_name, damage=int(dmg), health=int(hlth))
    army[type].append(dragon)

army_average = {}
for (key, value) in army.items():
    army_average[key] = [0, 0, 0]
    for item in value:
        army_average[key][0] += item.get_damage()
        army_average[key][1] += item.get_health()
        army_average[key][2] += item.get_armor()
    army_average[key] = [x/len(value) for x in army_average[key]]

for dragons in army.values():
    dragons.sort(key=lambda x: x.name)

for (type, dragons) in army.items():
    print(f"{type}::({army_average[type][0]:.2f}/{army_average[type][1]:.2f}/{army_average[type][2]:.2f})")
    for dragon in dragons:
        print(f"-{dragon.get_name()} -> damage: {dragon.get_damage()}, health: {dragon.get_health()}, armor: {dragon.get_armor()}")

