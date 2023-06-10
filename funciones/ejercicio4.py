"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
 devolver el total de la factura. Si se invoca la función sin pasarle el 
 porcentaje de IVA, deberá aplicar un 21%.
"""


def calculate_total(price, vat=20):
    return price + (price * vat / 100)


print(calculate_total(100000, 10))
