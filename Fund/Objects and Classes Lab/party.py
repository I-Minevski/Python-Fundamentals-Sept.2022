class Party:
    
    
    def __init__(self):
        self.people=[]

goers=Party()
while True:
    person=input()
    if person=="End":
        break
    goers.people.append(person)
print(f"Going: {', '.join(x for x in goers.people)}")
print(f"Total: {len(goers.people)}")