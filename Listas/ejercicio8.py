"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si 
es un palíndromo.
"""

word = input("Write a word: ")

# slicing python
# (inicio:fin:paso)
# Haker rank
# word_reversed = word[::-1]

word_reversed = list(word)
word_reversed.reverse()
word_reversed = "".join(word_reversed)

if word_reversed == word:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
