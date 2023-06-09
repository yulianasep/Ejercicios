"""
2. Escribir un programa que calcule la sumatoria de unos enteros dentro de una 
lista teniendo en cuenta un rango de numeros. Ejemplo:

Lista Original

[2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]

Rango (1,3) (incluyendo el 1 y 3)
Sumatoria de numeros dentro del rango: 6
"""

original_list = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
new_list = []

start = int(input("Enter the start of the range: "))
end = int(input("Enter the final of the range: "))

for i in range(len(original_list)):
    if original_list[i] >= start and original_list[i] <= end:
        new_list.append(original_list[i])


print(sum(new_list))
