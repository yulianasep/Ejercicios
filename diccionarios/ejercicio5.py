"""
Escribir un programa que almacene el diccionario con los créditos de las 
asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y 
después muestre por pantalla los créditos de cada asignatura en el formato 
<asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las 
asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar 
también el número total de créditos del curso.
"""

subjects = {
    'Math': 6,
    'Physics': 4,
    'Chemistry': 5
}

for key, value in subjects.items():
    print(f'{key} has {value} credits')

print(f'The total number of credits is {sum(subjects.values())}')
