"""
Escribir una función que reciba una muestra de números en una lista y devuelva 
un diccionario con su media, varianza y desviación típica.
"""


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    variance = 0
    for number in numbers:
        variance += (number - mean)**2
    return variance / len(numbers)


def calculate_standard_deviation(numbers):
    return calculate_variance(numbers)**0.5


def calculate_statistics(numbers):
    return {
        'mean': calculate_mean(numbers),
        'variance': calculate_variance(numbers),
        'standard_deviation': calculate_standard_deviation(numbers)
    }


print(calculate_statistics([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
