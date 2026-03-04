stock = input().split()

stock_dict = {}

for idx in range(0, len(stock), 2):
    key = stock[idx]
    value = stock[idx + 1]
    stock_dict[key] = int(value)

items_looking_for = input().split()

for product in items_looking_for:
    if product in stock_dict:
        print(f"We have {stock_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")