"""
Escribir una función que reciba una muestra de números en una lista y devuelva 
otra lista con sus cuadrados.
"""


def cuadrados(list_numbers):
    list_cuadrados = []
    for number in list_numbers:
        list_cuadrados.append(number**2)
    return list_cuadrados


print(cuadrados([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
