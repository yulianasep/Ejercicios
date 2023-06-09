"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

to_invest = float(input("Enter the amount of money you wish to invest\n"))
interest_rate = float(input("Enter the interest rate (in percentage)\n"))
years = int(input("Enter the number of years you wish to invest\n"))


for i in range(years):
    to_invest *= (1 + interest_rate/100)
    earned_interest = to_invest - to_invest/(1 + interest_rate/100)
    print(
        f"your investment for the year {i+1} was {round(to_invest-earned_interest)} what you earned in interest is {round((earned_interest), 2)}, your total amount is {round(to_invest)}")
