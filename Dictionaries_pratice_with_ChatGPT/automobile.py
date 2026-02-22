car = {
    "brand": "Honda",
    "model": "Accord",
    "year": "2008",
    "power": "201hp"
}
print(car.get("model"))
car["color"] = "silver"
for key, value in car.items():
    print(key, "->", value)