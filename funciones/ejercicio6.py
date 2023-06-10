"""
Escribir una función que reciba una muestra de números en una lista y devuelva 
su media.
"""


def list_numbers(list):
    sum_numbers = sum(list)
    return sum_numbers / len(list)


print(list_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
