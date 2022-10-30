activities=[0]*100
while True:
    note=input()
    if note=="End":
        break
    todo=note.split("-")
    activities.pop(int(todo[0]))
    activities.insert(int(todo[0]), todo[1])
activities=[x for x in activities if x!=0]
print(activities)
    