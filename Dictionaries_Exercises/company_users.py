company_users = {}

while True:
    command = input()
    if command == "End":
        break
    company_name, user_id = command.split(" -> ")
    company_users.setdefault(company_name, [])

    if user_id not in company_users[company_name]:
        company_users[company_name].append(user_id)

for company, user_list in company_users.items():
    print(company)
    for user in user_list:
        print(f"-- {user}")