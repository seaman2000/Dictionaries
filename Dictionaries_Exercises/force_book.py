force_book = {}

while True:
    user_exists = False
    input_line = input()

    if input_line == "Lumpawaroo":
        break

    if "|" in input_line:
        side, user = input_line.split(" | ")
        force_book.setdefault(side, [])

        for users in force_book.values():
            if user in users:
                user_exists = True

        if not user_exists:
            force_book[side].append(user)

    elif "->" in input_line:
        user, side = input_line.split(" -> ")
        for users in force_book.values():
            if user in users:
                users.remove(user)
                break
        force_book.setdefault(side, []).append(user)
        
        print(f"{user} joins the {side} side!")

print(force_book)