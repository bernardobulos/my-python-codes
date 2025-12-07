# Faça um programa que leia um ano qualquer e mostre se ele é bissexto. 🇧🇷
# Write a program that reads any given year and determines if it is a leap year. 🇺🇸
# Escriba un programa que lea cualquier año dado y determine si es un año bisiesto. 🇪🇸
# Écrivez un programme qui lit une année donnée et détermine s'il s'agit d'une année bissextile. 🇫🇷

from datetime import date

year = int(input("Enter any year (enter 0 to analyze the current year): "))
if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")
