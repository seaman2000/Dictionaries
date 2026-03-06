legendary_resources = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

legendary_is_obtained = False
while not legendary_is_obtained:
    items = input().split()

    for item in range(0, len(items), 2):
        quantity = int(items[item])
        material = items[item + 1].lower()

        legendary_resources[material] = legendary_resources.get(material, 0)
        legendary_resources[material] += quantity

        if legendary_resources["shards"] >= 250:
            print("Shadowmourne obtained!")
            legendary_resources["shards"] -= 250
            legendary_is_obtained = True
        elif legendary_resources["fragments"] >= 250:
            print("Valanyr obtained!")
            legendary_resources["fragments"] -= 250
            legendary_is_obtained = True
        elif legendary_resources["motes"] >= 250:
            print("Dragonwrath obtained!")
            legendary_resources["motes"] -= 250
            legendary_is_obtained = True

        if legendary_is_obtained:
            break

for resource, quantity in legendary_resources.items():
    print(f"{resource} : {quantity}")