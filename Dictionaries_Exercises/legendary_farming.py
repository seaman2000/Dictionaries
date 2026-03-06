legendary_resources = {
    "Shards": 0,
    "Fragments": 0,
    "Motes": 0
}
legendary_is_obtained = False
while True:
    quantity = int(input())
    material = input()
    legendary_resources[material] = legendary_resources.get(material, 0)
    legendary_resources[material] += quantity

    if legendary_resources["Shards"] >= 250:
        print("Shadowmourne obtained!")
        legendary_resources["Shards"] -= 250
        legendary_is_obtained = True
    elif legendary_resources["Fragments"] >= 250:
        print("Valanyr obtained!")
        legendary_resources["Fragments"] -= 250
        legendary_is_obtained = True
    elif legendary_resources["Motes"] >= 250:
        print("Dragonwrath obtained!")
        legendary_resources["Motes"] -= 250
        legendary_is_obtained = True

    if legendary_is_obtained:
        break

for resource, quantity in