"""
Durante el desarrollo de un pequeño videojuego se te encarga configurar y 
balancear cada clase de personaje jugable. Partiendo que la estadística base 
es 2, debes cumplir las siguientes condiciones:

El caballero tiene el doble de vida y defensa que un guerrero.
El guerrero tiene el doble de ataque y alcance que un caballero.
El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su 
defensa y el doble de su alcance.
Muestra como quedan las propiedades de los tres personajes.
"""

base = 2

characters = {
    'knight': {
        'life': 2 * base,
        'attack': base,
        'defense': 2 * base,
        'range': base
    },
    'warrior': {
        'life': base,
        'attack': 2 * base,
        'defense': base,
        'range': 2 * base
    },
    'archer': {
        'life': base,
        'attack': 2 * base,
        'defense': base / 2,
        'range': 2 * base
    }
}

for character, stats in characters.items():
    print(f"Properties of the {character}:")
    print(f"Life: {stats['life']}")
    print(f"Attack: {stats['attack']}")
    print(f"Defense: {stats['defense']}")
    print(f"Range: {stats['range']}")
    print()
