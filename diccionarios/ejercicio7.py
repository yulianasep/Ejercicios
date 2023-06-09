"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al 
diccionario, hasta que el usuario decida terminar. Después se debe mostrar 
por pantalla la lista de la compra y el coste total, con el siguiente formato
"""

shopping_cart = {}
total = 0

while True:
    item = input('Enter the item or write exit to finish: ')
    if item == 'exit':
        break
    price = float(input('Enter the price: '))
    shopping_cart[item] = price

for item, price in shopping_cart.items():
    total += price

print('Shopping cart:', shopping_cart)
print('Total:', total)
