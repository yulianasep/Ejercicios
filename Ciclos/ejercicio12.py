"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

sentence = (input("Enter a sentence: \n")).lower()
letter = input("Enter a letter: \n")
count = 0

for i in sentence:
    if i == letter.lower():
        count += 1

print(f"{letter} is in {count} places in ///{sentence}///.")
