def add_lesson(arr, title):
    if title not in arr:
        arr.append(title)
    return arr


def insert_lesson(arr, title, index):
    if title not in arr:
        arr.insert(int(index), title)
    return arr


def remove_lesson(arr, title):
    if title in arr:
        title_index=arr.index(title)
        if title_index in range(len(arr)):
            if "Excercise" in arr[title_index+1]:
                arr.pop(title_index+1)
        arr.remove(title)
    return arr


def swap_lesson(arr, title1, title2):
    if title1 in arr and title2 in arr:
        ind1=arr.index(title1)
        ind2=arr.index(title2)
        ex1_exists=False
        ex2_exists=False
        if ind1+1 in range(len(arr)):
            ex1_exists="Exercise" in arr[ind1+1] #proverka dali ima duma v stringa, ako ima vrushta True
        if ind2+1 in range(len(arr)):
            ex2_exists="Exercise" in arr[ind2+1]
        arr[ind1], arr[ind2] = arr[ind2], arr[ind1]
        if ex1_exists and ex2_exists:
            arr[ind1+1], arr[ind2+1] = arr[ind2+1], arr[ind1+1]
        elif not ex1_exists and ex2_exists:
            arr.insert(ind1+1, arr.pop(ind2+1)) #uprajnenieto e na 2rata poziciq + 1, a uroka veche e premesten na 1vata poziciq
            #popa e iztril vtoroto i ednovremenno vrushta stoinostta mu za da q slojim ladeto trqbva
        elif ex1_exists and not ex2_exists:
            arr.insert(ind2+1, arr.pop(ind1+1))
    return arr


def exercise(arr, title):
    if title in arr:
        if f"{title}-Exercise" not in arr:
            title_index=arr.index(title)
            arr.insert(title_index+1, f"{title}-Exercise")
    elif title not in arr:
        arr.append(title)
        arr.append(f"{title}-Exercise")
    return arr


lessons=input().split(", ")
while True:
    command=input()
    if(command=="course start"):
        break 
    com_list=command.split(":")
    action=com_list[0]
    lesson_title=com_list[1]
    if len(com_list)>2:
        title_or_index=com_list[2]
    
    if action=="Add":
        lessons=add_lesson(lessons, lesson_title)
    elif action=="Insert":
        lessons=insert_lesson(lessons, lesson_title, int(title_or_index))
    elif action=="Remove":
        lessons=remove_lesson(lessons, lesson_title)
    elif action=="Swap":
        lessons=swap_lesson(lessons, lesson_title, title_or_index)
    elif action=="Exercise":
        exercise(lessons, lesson_title)

num=1
for i in range(len(lessons)):
    print(f"{num}.{lessons[i]}")
    num+=1