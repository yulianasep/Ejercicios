"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al 
usuario la nota que ha sacado en cada asignatura, y después las muestre por 
pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
es cada una des las asignaturas de la lista y <nota> cada una de las 
correspondientes notas introducidas por el usuario.
"""

subjects = ["Math", "Physics", "Chemistry", "History", "Language"]
grades = []

for subject in subjects:
    grade = input(f"What grade did you get in {subject}? ")
    grades.append(grade)

for i in range(len(subjects)):
    print(f"In {subjects[i]} you got {grades[i]}")