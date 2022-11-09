from collections import OrderedDict


contest_passwords = {}
while True:
    cont_info = input().split(":")
    if cont_info[0] == "end of contests":
        break
    contest, password = cont_info
    if contest not in contest_passwords.keys():
        contest_passwords[contest] = password

users = {}
while True:
    user_info = input().split("=>")
    if user_info[0] == "end of submissions":
        break
    contest, password, username, points = user_info
    points = int(points)
    if contest in contest_passwords.keys():
        if password == contest_passwords[contest]:
            if username not in users.keys():
                users[username] = {}
            if contest not in users[username]:
                users[username][contest] = points
            else:
                if points > users[username][contest]:
                    users[username][contest] = points

scores = {}
for (key, value) in users.items():
    score = sum(users[key].values())
    scores[key] = score
best = max(scores.values())
for (key, value) in scores.items():
    if value == best:
        print(f"Best candidate is {key} with total {value} points.")

sorted_by_names = OrderedDict(sorted(users.items())) #sortirane po key
print("Ranking:")
for key in sorted_by_names.keys():
    print(key)
    sorted_by_values = sorted(sorted_by_names[key].items(), key=lambda x:x[1], reverse=True) #sortirane po value
    converted_dict = dict(sorted_by_values)
    for (contest, points) in converted_dict.items():
        print(f"#  {contest} -> {points}")
