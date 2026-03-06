force_book = {}

while True:
    input_line = input()

    if input_line == "Lumpawaroo":
        break

    if "|" in input_line:
        side, user = input_line.split(" | ")

        user_exists = False
        for users in force_book.values():
            if user in users:
                user_exists = True
                break

        if not user_exists:
            force_book.setdefault(side, []).append(user)

    elif "->" in input_line:
        user, side = input_line.split(" -> ")

        for users in force_book.values():
            if user in users:
                users.remove(user)
                break

        force_book.setdefault(side, []).append(user)
        print(f"{user} joins the {side} side!")

for force, users in force_book.items():
    if users:
        print(f"Side: {force}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")