"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 
'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su 
símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

coin = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥'
}

user_coin = input('Introduce una divisa: ')
print(coin.get(user_coin.title(), 'this currency is not available'))
