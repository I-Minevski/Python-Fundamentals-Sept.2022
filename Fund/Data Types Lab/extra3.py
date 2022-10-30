key=int(input())
lines=int(input())
message=""
for code in range(lines):
    sym=input()
    crypt=chr(ord(sym)+key)
    message+=crypt
print(message)