"""
Обчислити по формулі
"""
import re
def validator(text):
    return bool(re.match("^[-+]{0,1}\d*$", text))
def numbers(prompt):
    text = input(prompt)
    while not validator(text):
        text = input(prompt)
    return int(text)
def main():
    n = numbers("Введіть кількість ітерацій: ")
    x = numbers("Введіть змінну: ")
    for i in range (1, n+1):
        d = 1
        d *= x**i+i
        return d
print(main())