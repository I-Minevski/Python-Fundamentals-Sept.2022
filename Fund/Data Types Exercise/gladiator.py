lost=int(input())
helmet=float(input())
sword=float(input())
shield=float(input())
armor=float(input())
shield_breakings=0
total_cost=0
for battle in range(1, lost+1):
    if battle%2==0:
        total_cost+=helmet
    if battle%3==0:
        total_cost+=sword
    if battle%6==0:
        total_cost+=shield
        shield_breakings+=1
        if shield_breakings!=0 and shield_breakings%2==0:
            total_cost+=armor
print(f"Gladiator expenses: {total_cost:.2f} aureus")