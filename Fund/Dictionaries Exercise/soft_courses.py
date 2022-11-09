courses={}
while True:
    info=input().split(" : ")
    if info[0]=="end":
        break
    course_name=info[0]
    student=info[1]
    if course_name not in courses:
        courses[course_name]=[]
    courses[course_name].append(student)
for (key, value) in courses.items():
    print(f"{key}: {len(courses[key])}")
    for student in courses[key]:
        print(f"-- {student}")