"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""

number = int(input("Enter a number: \n"))
is_prime = True

if number < 2:
    is_prime = False

else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number")

else:
    print(f"{number} is not a prime number")
