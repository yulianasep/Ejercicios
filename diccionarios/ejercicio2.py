"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y 
teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el 
mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de 
teléfono es <teléfono>.
"""

user = {
    'name': input('Enter your name: '),
    'age': input('Enter your age: '),
    'address': input('Enter your address: '),
    'phone': input('Enter your phone: ')
}
print(f'Hi {user["name"]} you have {user["age"]} years old, you live in \
{user["address"]} and your phone number is {user["phone"]}')
