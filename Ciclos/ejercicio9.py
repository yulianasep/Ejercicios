"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

correct_password = "hola"
user_password = input("Enter your password \n")

while user_password != correct_password:
    user_password = input("Incorrect password, try again \n")
print("Congrats!! correct password")
