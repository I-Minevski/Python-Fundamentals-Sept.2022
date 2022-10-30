golemaduma=input()
duma=golemaduma.lower()
z="zzzzz"
br=0
duma+=z
words=["sand", "water", "fish", "sun"]
for sym in range(len(duma)-4):
    if duma[sym:sym+3] in words or duma[sym:sym+4] in words or duma[sym:sym+5] in words:
        br+=1
print(br)