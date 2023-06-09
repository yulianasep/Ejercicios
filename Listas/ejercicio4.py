"""
Escribir un programa que pregunte al usuario los números ganadores de la 
lotería primitiva, los almacene en una lista y los muestre por pantalla 
ordenados de menor a mayor.
"""

input_winning_numbers= input(
    "Please enter the winning numbers of the lottery separated by commas: ")
numbers = input_winning_numbers.split(",")
winning_numbers = []

for number in numbers:
    winning_numbers.append(int(number))
    winning_numbers.sort()

print(f"The lottery winning numbers are {winning_numbers}")
