book = {}
while True:
    info=input().split("-")
    if len(info)==1:
        break
    person=info[0]
    number=info[1]
    book[person]=number
n=int(info[0])
for i in range(n):
    name=input()
    if name in book.keys():
        print(f"{name} -> {book[name]}")
    else:
        print(f"Contact {name} does not exist.")