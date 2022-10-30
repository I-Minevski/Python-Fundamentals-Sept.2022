people=[int(number) for number in input().split(", ")]
minimum_wealth=int(input())
communism_working=True
for i in range(len(people)-1):
    index=people.index(max(people))
    if people[i]<minimum_wealth:
        diff=minimum_wealth-people[i]
        if people[index]-diff<minimum_wealth:
            print("No equal distribution possible")
            communism_working=False
            break
        people[i]+=diff
        people[index]-=diff
if communism_working==True:
    print(people)