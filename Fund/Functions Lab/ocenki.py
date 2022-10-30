def grading(a):
    if a>=2 and a <3:
        print("Fail")
    elif a>=3 and a <3.5:
        print("Poor")
    elif a>=3 and a <3.5:
        print("Poor")
    elif a>=3.5 and a <4.5:
        print("Good")
    elif a>=4.5 and a <5.5:
        print("Very Good")
    elif a>=5.5 and a <=6:
        print("Excellent")
        
grade=float(input())
grading(grade)