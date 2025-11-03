# Escreva um programa que leia um valor em metros e o exiba convertido em quilômetros, hectômetros, decâmetros, decímetros, centímetros e milímetros. 🇧🇷
# Write a program that reads a value in meters and displays it converted to kilometers, hectometers, decameters, decimeters, centimeters and millimeters. 🇺🇸
# Escribe un programa que lea un valor en metros y lo muestre convertido a kilómetros, hectómetros, decámetros, decímetros, centímetros y milímetros. 🇪🇸
# Écrivez un programme qui lit une valeur en mètres et l'affiche convertie en kilomètres, hectomètres, décamètres, décimètres, centimètres et millimètres. 🇫🇷

m = float(input("Enter a distance in meters: "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f"""The distance {m} meters corresponds to:
 — {km:.2f} kilometers.
 — {hm:.2f} hectometers.
 — {dam:.2f} decameters.
 — {dm:.2f} decimeters.
 — {cm:.2f} centimeters.
 — {mm:.2f} millimeters.""")
