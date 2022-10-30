rooms=int(input())
free=0
conditions_met=True
number=1
while number<=rooms:
    room_info=input().split(" ")
    chairs=len(room_info[0])
    people=int(room_info[1])
    if chairs>=people:
        free+=(chairs-people)
    else:
        conditions_met=False
        print(f"{people-chairs} more chairs needed in room {number}")
    number+=1
if conditions_met==True:
    print(f"Game On, {free} free chairs left")