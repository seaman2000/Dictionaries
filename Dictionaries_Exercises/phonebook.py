phone_book = {}

while True:
    current_contact = input()
    if "-" not in current_contact:
        break
    name, number = current_contact.split("-")
    phone_book[name] = number

number_of_searches = int(current_contact)
for _ in range(number_of_searches):
    calling_name = input()
    if calling_name in phone_book:
        print(f"{calling_name} -> {phone_book[calling_name]}")
    else:
        print(f"Contact {calling_name} does not exist.")