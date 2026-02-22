user = {"name": "Georgi", "age": 20, "city": "Burgas"}
print(user.get("name"))
user["job"] = "Programmer"

for key, value in user.items():
    print(key, "->", value)