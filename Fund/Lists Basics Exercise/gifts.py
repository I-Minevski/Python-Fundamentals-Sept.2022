gifts_seq=input()
gifts=gifts_seq.split(" ")
while True:
    command=input()
    if command=="No Money":
        break
    if "OutOfStock" in command:
        gift_name=command[11::]
        #print(gift_name)
        for i in range(len(gifts)):
            if gifts[i]==gift_name:
                gifts[i]="None"
    if "JustInCase" in command:
        gift_name=command[11::]
        #print(gift_name)
        gifts[len(gifts)-1]=gift_name
    if "Required" in command:
        required_list=command.split(" ")
        #print(required_list)
        index=int(required_list[2])
        if 0<=index<abs(len(gifts)):
            gifts[index]=required_list[1]
for i in range(len(gifts)):
    if gifts[i]!="None":
        print(gifts[i], end=" ")
        