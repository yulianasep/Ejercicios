"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con 
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, 
correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada 
un nuevo dato debe imprimirse el contenido del diccionario.
"""

user = {}

while True:
    key = input('Enter the key: ')
    value = input('Enter the value: ')
    user[key] = value
    print(user)
    if input('Do you want to continue? (y/n) ') == 'n':
        break

print(user)
