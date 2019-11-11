"""
Підрахувати кількість цілих серед чисел а, b, с (ввести з клавіатури).
"""
import re
def number(text):
    return bool(re.match("^[-+]{0,1}\d*$", text))
def get_number(prompt):
    text = input(prompt)
    while not number(text):
        return "Не ціле число"
    return text

def checker():
    a = get_number("Перше число: ")
    b = get_number("Друге число: ")
    c = get_number("Третє число: ")
    return a, b, c
print(checker())