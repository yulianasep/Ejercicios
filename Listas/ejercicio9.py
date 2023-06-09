"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el 
número de veces que contiene cada vocal.
"""

word = input("Write a word: ")
vowels = {"a", "e", "i", "o", "u"}

for vowel in vowels:
    print(f"{vowel}: {word.count(vowel)}")
