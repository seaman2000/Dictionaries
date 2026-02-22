cars = {
    "BMW": 250,
    "Audi": 220,
    "Honda": 201,
    "Mercedes": 270
}
max_hp = 0
car_model = ""
for key, value in cars.items():
    if value > max_hp:
        max_hp = value
        car_model = key

print(f"The fastest car between is {car_model} with {max_hp}")