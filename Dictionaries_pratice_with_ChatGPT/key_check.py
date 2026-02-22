product = {
    "name": "Laptop",
    "price": 1500,
    "brand": "Lenovo"
}
if "discount"not in product:
    product["discount"] = 10

price = product["price"]
discount = product["discount"]
total_price = price - (price * discount / 100)

print(round(total_price, 2))