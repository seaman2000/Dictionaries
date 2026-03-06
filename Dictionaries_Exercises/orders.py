items_list = {}

while True:
    current_product = input()

    if current_product == "buy":
        break

    name, price, quantity = current_product.split()
    price = float(price)
    quantity = int(quantity)

    if name not in items_list.keys():
        items_list[name] = [price, quantity]
    else:
        items_list[name][1] += quantity
        items_list[name][0] = price


for key, lst in items_list.items():
    result = lst[1] * lst[0]
    items_list[key] = result
    print(f"{key} -> {result:.2f}")
