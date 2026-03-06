company_users = {}

while True:
    command = input()
    if command == "end":
        break
    company_name, user_id = command.split(" -> ")