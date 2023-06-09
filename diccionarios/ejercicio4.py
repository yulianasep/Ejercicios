"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre 
por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el 
nombre del mes.
"""

months = {
    '01': 'Enero',
    '02': 'Febrero',
    '03': 'Marzo',
    '04': 'Abril',
    '05': 'Mayo',
    '06': 'Junio',
    '07': 'Julio',
    '08': 'Agosto',
    '09': 'Septiembre',
    '10': 'Octubre',
    '11': 'Noviembre',
    '12': 'Diciembre'
}

date = input('Enter a date in format dd/mm/yyyy: ')
date = date.split('/')
print(f'{date[0]} de {months[date[1]]} de {date[2]}')
