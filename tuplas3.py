"""
3. Escribir un programa que determine si un string ingresado por el usuario 
esta dentro una tupla de tuplas conteniendo strings. Ejemplo:

(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 
'Lime'))

Ingresa el elemento a buscar: White
True
"""

tuple = (('Red', 'White', 'Blue'), ('Green', 'Pink',
         'Purple'), ('Orange', 'Yellow', 'Lime'))

elemento = input("Enter the item to search for: ").title()

for i in range(len(tuple)):
    if elemento in tuple[i]:
        print(True)
        break
else:
    print(False)
