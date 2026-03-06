line = input()
char_dictionary = {}

for char in line:
    if " " in char:
        continue
    char_dictionary.setdefault(char, 0)
    char_dictionary[char] += 1

for key, value in char_dictionary.items():
    print(f"{key} -> {value}")