"""
Escribir un programa que reciba una cadena de caracteres y devuelva un 
diccionario con cada palabra que contiene y su frecuencia. Escribir otra 
función que reciba el diccionario generado con la función anterior y devuelva 
una tupla con la palabra más repetida y su frecuencia.
"""


def count_words(string):
    words = string.split()
    words_dict = {}
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict


def most_repeated(words_dict):
    max_word = ''
    max_freq = 0
    for word, freq in words_dict.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq


print(count_words('hola mundo adios mundo'))
print(most_repeated(count_words('hola mundo adios mundo')))
