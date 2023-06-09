"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
"""

number = int(input("Please enter a positive number \n"))

for i in range(1, (number+1), 2):
    for n in range(i, 0, -2):
        print(n, end=" ")
    print("")
