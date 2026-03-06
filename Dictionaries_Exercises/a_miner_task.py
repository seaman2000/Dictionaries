resources_and_quantities = {}

while True:
    current_resource = input()
    if current_resource == "stop":
        break
    current_quantity = int(input())
    resources_and_quantities.setdefault(current_resource, 0)
    resources_and_quantities[current_resource] += current_quantity

for resource, quantity in resources_and_quantities.items():
    print(f"{resource} -> {quantity}")