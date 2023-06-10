"""
Escribir una función que convierta un número decimal en binario y otra que 
convierta un número binario en decimal.
"""


def decimal_binary(number):
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary


def binary_decimal(number):
    decimal = 0
    for i, digit in enumerate(reversed(str(number))):
        decimal += int(digit) * 2**i
    return decimal


print(decimal_binary(10))
print(binary_decimal(1010))
