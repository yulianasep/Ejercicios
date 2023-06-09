"""
Escribir un programa que almacene las matrices
en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, 
representando cada vector fila en una lista.
"""

matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
    [-1, 0],
    [0, 1],
    [1, 1]
]

matrix_c = []

for i in matrix_a:
    print(i)
    for x in i:
        print(x)
