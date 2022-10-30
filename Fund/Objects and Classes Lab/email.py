class Email:
    
    
    def __init__(self, sender, receiver, content):
        self.sender=sender
        self.receiver=receiver
        self.content=content
        self.is_true=False
    
    def send(self):
        self.is_true=True
        return self.is_true
    
    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_true}"
    

emails=[]
while True:
    info=input()
    if info=="Stop":
        break
    elements=info.split(" ")
    message=Email(elements[0], elements[1], elements[2])
    emails.append(message)
sent=list(map(lambda x: int(x), input().split(", ")))

#sent=input().split(", ")
#sent=[int(x) for x in sent] 
#moje i na 2 reda ochevidno ama s taq lambda e mn fancy

for i in sent:
    emails[i].send()
for i in emails:
    print(i.get_info())