spots={}
n=int(input())
for i in range(n):
    command=input().split(" ")
    if "register" in command:
        username=command[1]
        license=command[2]
        if username in spots.keys():
            print(f"ERROR: already registered with plate number {spots[username]}")
        else:
            spots[username]=license
            print(f"{username} registered {license} successfully")
    if "unregister" in command:
        username=command[1]
        if username in spots.keys():
            del spots[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")
for (key, value) in spots.items():
    print(f"{key} => {value}")