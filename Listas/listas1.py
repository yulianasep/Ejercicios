"""
1. Escribir un programa para eliminar una lista de palabras de una lista de 
strings. Ejemplo:

Lista Original:
['Red color', 'Orange#', 'Green', 'Orange @', 'White']

Lista de elementos a eliminar:
['#', 'color', '@']

Resultado:
['Red', '', 'Green', 'Orange', 'White']
"""

original_list = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
delete_list = ['#', 'color', '@']

for i in range(len(original_list)):
    for j in range(len(delete_list)):
        original_list[i] = original_list[i].replace(delete_list[j], '')

print(original_list)
