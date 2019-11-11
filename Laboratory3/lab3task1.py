"""
Заміна вибраного символа на інший
"""
import re
def int_validator(text):
    n = input(text)
    while not bool(re.match(r'^\d+$', n)):
        n = input(text)
    return int(n)
def string_validator(text):
    string = input(text)
    while bool(re.match(r'^\s*$', string)):
        string = input(text)
    return string
data = string_validator('Enter text: ')
n = int_validator('Enter n: ')
what = string_validator('What do you  want to change: ')
to = string_validator('Change on what: ')
split_string = data.split()
print("\nОкремі слова в рядку: ", split_string)
new_string_list = list()
for word in split_string:
    if len(word) < n:
        k = 0
        word_characters = list(word)
        for i in word_characters:
            if i == what:
                word_characters[k] = to
            k = k + 1
        new_word = "".join(word_characters)
        new_string_list.append(new_word)
    else:
        new_string_list.append(word)
new_string = " ".join(new_string_list)
print("\nРезультат: ", new_string)