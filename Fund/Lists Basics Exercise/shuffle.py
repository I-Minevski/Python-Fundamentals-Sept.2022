from re import U


seq=input()
deck=seq.split(" ")
number=int(input())
for shuffles in range(number):
    upperhalf=deck[:int(len(deck)/2):]
    lowerhalf=deck[int(len(deck)/2)::]
    new_deck=[]
    for i in range(len(upperhalf)):
        new_deck.append(upperhalf[i])
        new_deck.append(lowerhalf[i])
    deck=new_deck
print(deck)