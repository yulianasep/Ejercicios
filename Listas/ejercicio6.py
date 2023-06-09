"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al 
usuario la nota que ha sacado en cada asignatura y elimine de la lista las 
asignaturas aprobadas. Al final el programa debe mostrar por pantalla las 
asignaturas que el usuario tiene que repetir.
"""

subjects = ["Math", "Physics", "Chemistry", "History", "Language"]
grades = []
subjects_repeating = []


for subject in subjects:
   grade = int(input(f"What grade did you get in {subject}? "))
   grades.append(grade) 

for i in range(len(grades)):
   if grades[i] < 3:
    subjects_repeating.append(subjects[i])

print(f"You have to repeat the following subjects: {subjects_repeating}.")