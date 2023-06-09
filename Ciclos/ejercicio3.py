"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

number = int(input("Please enter a positive number \n"))

for i in range(1, (number), 2):
    print(i, end=", ")
