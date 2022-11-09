companies={}
while True:
    info=input().split(" -> ")
    if info[0]=="End":
        break
    company_name=info[0]
    user_id=info[1]
    if company_name not in companies:
        companies[company_name]=[]
    if user_id not in companies[company_name]:
        companies[company_name].append(user_id)
for (key, value) in companies.items():
    print(key)
    for employee in companies[key]:
        print(f"-- {employee}")