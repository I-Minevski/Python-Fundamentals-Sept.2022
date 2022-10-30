import math


students=int(input())
lectures=int(input())
additional=int(input())
attendance=[]
for i in range(students):
    x=int(input())
    attendance.append(x)
bonus=[]
for i in range(len(attendance)):
    bonus.append((attendance[i]/lectures)*(5+additional))
maxel=max(bonus)
maxind=bonus.index(maxel)
print(f"Max Bonus: {math.ceil(maxel)}.")
print(f"The student has attended {attendance[maxind]} lectures.")