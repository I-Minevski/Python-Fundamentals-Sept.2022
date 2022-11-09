students={}
info=input().split(":")
while len(info)>1:
    name, id, course = info[0], info[1], info[2]
    if course not in students.keys():
        students[course]=[]
    students[course].append(f"{name} - {id}")
    info=input().split(":")
searched_course = info[0].replace("_", " ")
for student in students[searched_course]:
    print(student)