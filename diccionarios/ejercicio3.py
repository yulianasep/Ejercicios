"""
Escribir un programa que guarde en un diccionario los precios de las frutas de 
la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por 
pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el 
diccionario debe mostrar un mensaje informando de ello.
"""

fruits = {
    'banana': 1.35,
    'apple': 0.80,
    'pear': 0.85,
    'orange': 0.70
}

fruit = input('Enter a fruit: ')
kg = float(input('Enter the weight in kg: '))

if fruit in fruits:
    print(f'{kg} kg of {fruit} cost {round((fruits[fruit] * kg),2)}')

else:
    print(f'{fruit} is not available')
