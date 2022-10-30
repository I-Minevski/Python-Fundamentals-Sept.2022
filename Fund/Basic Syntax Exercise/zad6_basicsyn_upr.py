n=int(input())
for i in range(n):
    pureness=True
    word=input()
    if "," in word or "." in word or "_" in word:
        pureness=False
    if pureness==True:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")