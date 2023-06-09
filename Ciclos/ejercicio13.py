"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""

eco = input(
    "Enter a word and you will hear the ECO, if you want to exit, type exit: ")

while eco != "exit":
    print(eco)
    eco = input(
        "Enter a word and you will hear the ECO, if you want to exit, type exit: ")
