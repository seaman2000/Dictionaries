words_in_line = input().split()
odd_dict = {}

for word in words_in_line:
    lower_word = word.lower()
    if lower_word not in odd_dict:
        odd_dict[lower_word] = 0
    odd_dict[lower_word] += 1

for key, value in odd_dict.items():
    if value % 2 == 1:
        print(key, end=' ')
