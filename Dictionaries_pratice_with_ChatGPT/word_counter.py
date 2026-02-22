text = "python is easy and python is powerful"
text_list = text.split()
dictionary = {}
for word in text_list:
    dictionary[word] = dictionary.get(word, 0) + 1
print (dictionary)