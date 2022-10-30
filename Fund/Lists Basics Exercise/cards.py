seq=input()
cards=seq.split(" ")
teamA=teamB=11
removedA=[]
removedB=[]
for i in range(len(cards)):
    if "A" in cards[i] and cards[i] not in removedA:
        teamA-=1
        removedA.append(cards[i])
    if "B" in cards[i] and cards[i] not in removedB:
        teamB-=1
        removedB.append(cards[i])
    if teamA<7 or teamB<7:
        break
print(f"Team A - {teamA}; Team B - {teamB}")
if teamA<7 or teamB<7:
    print("Game was terminated")