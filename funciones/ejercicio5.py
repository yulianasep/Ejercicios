"""
Escribir una función que calcule el área de un círculo y otra que calcule el 
volumen de un cilindro usando la primera función.
"""

from math import pi


def area_circle(radius):
    return pi * radius ** 2


def volume_cylinder(radius, height):
    return area_circle(radius) * height


print(volume_cylinder(5, 10))
