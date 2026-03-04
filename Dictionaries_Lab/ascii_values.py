list_of_characters = input().split(", ")

char_dict = {char: ord(char) for char in list_of_characters}

print( char_dict)


