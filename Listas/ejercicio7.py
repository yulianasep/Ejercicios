"""
Escribir un programa que almacene el abecedario en una lista, elimine de la 
lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla 
la lista resultante.
"""

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i",
    "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
    "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

new_alphabet = []

for i in range(len(alphabet)):
    if (i+1) % 3 != 0:
        new_alphabet.append(alphabet[i])

print(new_alphabet)
