food = input().split()

food_dict = {}

for idx in range(0, len(food), 2):
    key = food[idx]
    value = food[idx + 1]
    food_dict[key] = int(value)

print(food_dict)