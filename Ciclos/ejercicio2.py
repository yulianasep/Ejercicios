"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

age = int(input("Enter you age \n"))

for i in range(age):
    print(f"Cumpliste {(i+1)} años")
