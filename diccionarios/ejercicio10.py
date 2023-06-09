"""
Escribir un programa que permita gestionar la base de datos de clientes de una 
empresa. Los clientes se guardarán en un diccionario en el que la clave de 
cada cliente será su NIF, y el valor será otro diccionario con los datos del 
cliente (nombre, dirección, teléfono, correo, preferente), donde preferente 
tendrá el valor True si se trata de un cliente preferente. El programa debe 
preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, 
(2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) 
Listar clientes preferentes, (6) Terminar. En función de la opción elegida el 
programa tendrá que hacer lo siguiente:

    1.Preguntar los datos del cliente, crear un diccionario con los datos y 
    añadirlo a la base de datos.
    2.Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    3.Preguntar por el NIF del cliente y mostrar sus datos.
    4.Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    5.Mostrar la lista de clientes preferentes de la base de datos con su NIF 
    y nombre.
    6.Terminar el programa.

"""

clients = {}
nif_request = "Enter the customer's NIF: "

while True:
    print("Welcome to the database, here are the options"
          "\n1. Add client"
          "\n2. Remove client"
          "\n3. Show client"
          "\n4. List all clients"
          "\n5. List preferred clients"
          "\n6. End")
    option = input("Enter an option: ")

    if option == "6":
        break

    if option == "1":
        nif = input(nif_request)
        name = input("Enter the customer's name: ")
        address = input("Enter the customer's address: ")
        phone = input("Enter customer's phone number: ")
        email = input("Enter customer's email address: ")
        vip = input("Are you a preferred customer (Y/N)? ")

        client = {'name': name, 'address': address, 'phone': phone,
                  'email': email, 'preferred': vip == 'Y'}
        clients[nif] = client

    elif option == "2":
        nif = input(nif_request)
        if nif in clients:
            del clients[nif]
        else:
            print("The client with the nif does not exist", nif)

    if option == "3":
        nif = input(nif_request)
        if nif in clients:
            print("NIF:", nif)
            for key, value in clients[nif].items():
                print(key.title() + ":", value)
        else:
            print("The client with the nif does not exist", nif)

    elif option == "4":
        print("List of clients")
        for key, value in clients.items():
            print(key, value["name"])

    elif option == "5":
        print("List of preferred clients")
        for key, value in clients.items():
            if value["preferred"]:
                print(key, value["name"])

    else:
        print("Wrong option")
