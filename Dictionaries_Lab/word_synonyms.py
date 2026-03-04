number_of_words = int(input())
my_dict = {}

for _ in range(number_of_words):
    word = input()
    synonym = input()

    if word in my_dict:
        my_dict[word].append(synonym)
    else:
        my_dict[word] = [synonym]

for key, value in my_dict.items():
    print(f"{key} - {', '.join(value)}")
