"""
Escribir un programa que gestione las facturas pendientes de cobro de una 
empresa. Las facturas se almacenarán en un diccionario donde la clave de cada 
factura será el número de factura y el valor el coste de la factura. El 
programa debe preguntar al usuario si quiere añadir una nueva factura, pagar 
una existente o terminar. Si desea añadir una nueva factura se preguntará por 
el número de factura y su coste y se añadirá al diccionario. Si se desea pagar 
una factura se preguntará por el número de factura y se eliminará del 
diccionario. Después de cada operación el programa debe mostrar por pantalla 
la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""

invoices = {}

while True:
    option = input(
        "Introduce 'a' para añadir una factura, 'p' para pagarla o 't' para "
        "terminar: ")
    if option == "t":
        break
    elif option == "a":
        key = input("Introduce el número de la factura: ")
        value = float(input("Introduce el coste de la factura: "))
        invoices[key] = value
    elif option == "p":
        key = input("Introduce el número de la factura a pagar: ")
        invoices.pop(key)
    else:
        print("Opción incorrecta")

print("Cantidad cobrada: ")
print(sum(invoices.values()))
print("Cantidad pendiente de cobro: ")
print(invoices)
