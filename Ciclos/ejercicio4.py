"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

number = int(input("Please enter a positive number \n"))

for i in range(number):
    print((number-i), end=", ")
