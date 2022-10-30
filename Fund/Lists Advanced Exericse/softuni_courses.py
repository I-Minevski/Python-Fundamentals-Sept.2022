courses=input().split(", ")
while True:
    command=input()
    if(command=="course start"):
        break 
    com_list=command.split(":")
    if "Add" in com_list and com_list[1] not in courses:
        courses.append(com_list[1])
    if "Insert" in com_list and com_list[1] not in courses:
        courses.insert(int(com_list[2]), com_list[1])
    if "Remove" in com_list and com_list[1] in courses:
        index=courses.index(com_list[1])
        if f"{com_list[1]}-Exercise" in courses:
            courses.remove(f"{com_list[1]}-Exercise")
        courses.remove(com_list[1])
    if "Swap" in com_list and com_list[1] in courses and com_list[2] in courses:
        ind1=courses.index(com_list[1])
        ind2=courses.index(com_list[2])
        if f"{com_list[1]}-Exercise" not in courses and f"{com_list[2]}-Exercise" not in courses:
            courses[ind1], courses[ind2] = courses[ind2], courses[ind1]
    if "Excercise" in com_list:
        if com_list[1] in courses:
            index=courses.index(com_list[1])
            if "Excercise" not in courses[index+1]:
                ex_name=f"{com_list[1]}-Exercise"
                courses.insert(index+1, ex_name)
        else:
            courses.append(com_list[1])
            courses.append(f"{com_list[1]}-Exercise")
num=1
for i in range(len(courses)):
    print(f"{num}.{courses[i]}")
    num+=1