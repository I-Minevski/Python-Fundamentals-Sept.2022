houses=[int(number) for number in input().split("@")]
cupid_index=0
while True:
    jump=input()
    if jump=="Love!":
        break
    jump_list=jump.split(" ")
    length=int(jump_list[1])
    if cupid_index + length in range(len(houses)):
        cupid_index+=length
    else:
        cupid_index=0
    if houses[cupid_index]>0:
            houses[cupid_index]-=2
            if houses[cupid_index]==0:
                print(f"Place {cupid_index} has Valentine's day." )
    else:
        print(f"Place {cupid_index} already had Valentine's day.")
print(f"Cupid's last position was {cupid_index}.")
if houses.count(0)==len(houses):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(houses)-houses.count(0)} places.")