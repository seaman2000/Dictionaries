items_dict = {}
while True:
    item = input()

    if item == "statistics":
        break

    current_item = item.split(": ")
    key = current_item[0]
    value = int(current_item[1])

    if key in items_dict:
        items_dict[key] += value
    else:
        items_dict[key] = value

products_count = len(items_dict)
products_quantity = sum(items_dict.values())

print("Products in stock:")
for key, value in items_dict.items():
    print(f"- {key}: {value}")

print(f"Total Products: {products_count}")
print(f"Total Quantity: {products_quantity}")
