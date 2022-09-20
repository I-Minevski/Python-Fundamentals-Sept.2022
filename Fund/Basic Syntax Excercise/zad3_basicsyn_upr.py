lines=int(input())
for i in range(lines):
    com=int(input())
    if com==88:
        print("Hello")
    elif com==86:
        print("How are you?")
    elif com<88:
        print("GREAT!")
    elif com>88:
        print("Bye.")