"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

"""

number = int(input("Please enter a positive number \n"))

for i in range(number):
    print("*"*(i+1))
