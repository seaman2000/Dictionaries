number_of_words = int(input())
words_dict = {}

for _ in range(number_of_words):
    word = input()
    synonym = input()

    words_dict.setdefault(word, []).append(synonym)

for word, synonym in words_dict.items():
    print(f"{word} - {', '.join(synonym)}")