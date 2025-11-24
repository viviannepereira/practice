import re

def find_word(string):
    word = re.findall(r"^(\w+)\s", string)
    return word[0]

print(find_word("Vivianne is cool"))