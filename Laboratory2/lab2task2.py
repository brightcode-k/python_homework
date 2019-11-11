"""
Написати програму, в результаті виконання якої з'ясується, чи входить цифра 2 в запис даного цілого числа n.
"""
import re
def checker(text):
    return bool(re.match("^[-+]?\d+\.{0,1}\d*$", text))
def get_number(prompt):
    text = input(prompt)
    while not checker(text):
        text = input(prompt)
    return text
def ch():
    n = checker("Введіть ціле число: ")
    ym = False
    for i in n:
        if i=="2":
            ym = True
            break
    return ym, "Так, в вашому записі є число 2"
print(ch())