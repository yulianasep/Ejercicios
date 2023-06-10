"""
Escribir una función que calcule el máximo común divisor de dos números y otra 
que calcule el mínimo común múltiplo.
"""


def mcd(number1, number2):
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1


def mcm(number1, number2):
    return number1 * number2 // mcd(number1, number2)


print(mcd(24, 36))
print(mcm(24, 36))
