"""
Escribir un programa que cree un diccionario de traducción español-inglés. 
El usuario introducirá las palabras en español e inglés separadas por dos 
puntos, y cada par <palabra>:<traducción> separados por comas. El programa 
debe crear un diccionario con las palabras y sus traducciones. Después pedirá 
una frase en español y utilizará el diccionario para traducirla palabra a 
palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

dictionary = {}

words = input(
    "Introduce las palabras en español e inglés separando con dos puntos ':' "
    "la palabra de su traducción y escribe ',' para introducir otra palabra ")
for i in words.split(","):
    key, value = i.split(":")
    dictionary[key] = value

sentence = input("Introduce una frase en español: ")

for i in sentence.split():
    if i in dictionary:
        print(dictionary[i], end=" ")
    else:
        print(i, end=" ")
