number_of_commands = int(input())
parking_lot_submissions = {}

for _ in range(number_of_commands):
    current_command = input().split()
    type_of_command = current_command[0]
    name = current_command[1]

    if type_of_command == "register":
        plate_number = current_command[2]

        if name in parking_lot_submissions:
            print(f"ERROR: already registered with plate number {parking_lot_submissions[name]}")
        else:
            parking_lot_submissions[name] = plate_number
            print(f"{name} registered {plate_number} successfully")

    elif type_of_command == "unregister":
        if name not in parking_lot_submissions:
            print(f"ERROR: user {name} not found")
        else:
            del parking_lot_submissions[name]
            print(f"{name} unregistered successfully")

for name, plate_num in parking_lot_submissions.items():
    print(f"{name} => {plate_num}")
