"""
Обчислити по формулі
"""
import math
import re
def check(text):
    return bool(re.match("^[-+]{0,1}\d*\.{0,1}\d*$", text))
def get_number(prompt):
    text = input(prompt)
    while not check(text):
        text = input(prompt)
    return float(text)
def counter():
    x = get_number("Введіть число та натисніть ENTER: ")
    if 0<=x<=1:
        v1 = pow(x, x)-x
        return round(v1, 3)
    else:
        v2 = pow(x, x)-math.sin(math.pi*pow(x, x))
        return round(v2, 3)
print("Result - ", counter())