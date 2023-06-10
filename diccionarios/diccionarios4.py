"""
4. Escribir un programa que a partir de una lista de nombres determine cuantas 
veces se repiten los nombres dentro de ella. Ejemplo:

Lista:
['Juan', 'Felipe', 'Santiago', 'Juan', 'Maria', 'Maria', 'Santiago', 'Maria', 
'Esteban', 'Laura']
 
Resultado:
{'Juan': 2, 'Felipe': 1, 'Santiago': 2, 'Maria': 3, 'Esteban': 1, 'Laura':1}
"""

list = ['Juan', 'Felipe', 'Santiago', 'Juan', 'Maria', 'Maria', 'Santiago',
        'Maria', 'Esteban', 'Laura']

dictionary = {}

for name in list:
    if name in dictionary:
        dictionary[name] += 1
    else:
        dictionary[name] = 1

print(dictionary)
