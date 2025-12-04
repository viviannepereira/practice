import re

def capture_vowel(string):
    words = re.findall(r"[aeiouAEIOU]+\w*\s", string)
    return words

print(capture_vowel("Its awesome. NOT!"))