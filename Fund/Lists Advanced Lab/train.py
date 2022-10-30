wagons=int(input())
train=[0]*wagons    #taka pulnim masiv s nuli (ili kvot da e drugo) ebasi qkoto a
while True:
    command=input()
    if command=="End":
        break
    com_list=command.split(" ")
    if "add" in command:
        train[wagons-1]+=int(com_list[1])
    if "insert" in command:
        train[int(com_list[1])]+=int(com_list[2])
    if "leave" in command:
        train[int(com_list[1])]-=int(com_list[2])
print(train)