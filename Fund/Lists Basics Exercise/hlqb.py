energy=100
coins=100
events=input().split("|")
is_completed=True
for i in range(len(events)):
    occ=events[i].split("-")
    event=occ[0]
    num=int(occ[1])
    if event=="rest":
        current_energy=energy
        energy+=num
        if energy>100:
            energy=100
        gained=energy-current_energy
        print(f"You gained {gained} energy.")
        print(f"Current energy: {energy}.")
    elif event=="order":
        if energy-30>=0:
            coins+=num
            energy-=30
            print(f"You earned {num} coins.")
        else:
            energy+=50
            print("You had to rest!")
    else:
        if coins>=num:
            print(f"You bought {event}.")
            coins-=num
        else:
            print(f"Closed! Cannot afford {event}.")
            is_completed=False
            break
if is_completed==True:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")