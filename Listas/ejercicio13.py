"""
Escribir un programa que pregunte por una muestra de números, separados por 
comas, los guarde en una lista y muestre por pantalla su media y desviación 
típica.
"""

from math import sqrt

numbers = input("Write a list of numbers separated by commas: ")
numbers = numbers.split(",")
# Comprensión de listas y diccionarios - condicionales
numbers = [int(x) for x in numbers]

# numbers2 = []
# for x in numbers:
#     numbers2.append(int(x))

mean = (sum(numbers))/len(numbers)

deviation = []

for number in numbers:
    diference = abs(number - mean)
    deviation.append(diference**2)

standard_deviation = round(((sum(deviation)/len(deviation))**0.5), 2)

print("The mean is: ", mean)
print("The standard deviation is: ", standard_deviation)
