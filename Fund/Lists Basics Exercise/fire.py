inferno=input()
fires=inferno.split("#")
water=int(input())
effort=0
total_fire=0
individual_fires=[]
for i in range(len(fires)):
    cell=fires[i].split(" ")
    cell[2]=int(cell[2])
    if "High" in cell:
        if cell[2]<81 or cell[2]>125:
            continue
    elif "Medium" in cell:
        if cell[2]<51 or cell[2]>80:
            continue
    elif "Low" in cell:
        if cell[2]<1 or cell[2]>50:
            continue
    if cell[2]<=water:
        water-=cell[2]
        effort+=25*0.01*cell[2]
        total_fire+=cell[2]
        individual_fires.append(cell[2])
    else:
        continue
print("Cells:")
for i in range(len(individual_fires)):
    print(f" - {individual_fires[i]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")