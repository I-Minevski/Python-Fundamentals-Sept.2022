dungeon=input().split("|")
health=100
bitcoins=0
is_complete=True
for i in range(len(dungeon)):
    room=dungeon[i].split(" ")
    command=room[0]
    amount=int(room[1])
    if command=="potion":
        if health+amount>100:
            print(f"You healed for {100-health} hp.")
            health=100
        else:
            print(f"You healed for {amount} hp.")
            health+=amount
        print(f"Current health: {health} hp.")
    elif command=="chest":
        print(f"You found {amount} bitcoins.")
        bitcoins+=amount
    else:
        if health-amount>0:
            print(f"You slayed {command}.")
            health-=amount
        else:
            print(f"You died! Killed by {command}." )
            print(f"Best room: {i+1}")
            is_complete=False
            break
if is_complete==True:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")