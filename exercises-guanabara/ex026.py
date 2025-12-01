# Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "A" e em que posição a letra "A" aparece na primeira vez e na última vez. 🇧🇷
# Write a program that reads a sentence from the keyboard and displays: how many times the letter "A" appears and in what position the letter "A" appears the first and last time. 🇺🇸
# Escriba un programa que lea una oración del teclado y muestre: cuántas veces aparece la letra "A" y en qué posición aparece la letra "A" la primera y la última vez. 🇪🇸
# Écrivez un programme qui lit une phrase au clavier et affiche : le nombre de fois où la lettre « A » apparaît et à quelle position la lettre « A » apparaît la première et la dernière fois. 🇫🇷

phrase = str(input("Enter a sentence: ")).strip()
quant_a = phrase.upper().count("A")
first_a = phrase.upper().find("A")
last_a = phrase.upper().rfind("A")

if quant_a == 1:
    print(f" – The letter \"A\" in the phrase \"{phrase}\" appears only once.")
else:
    print(f" – The letter \"A\" in the phrase \"{phrase}\" appears {quant_a} times.")
print(f" – The first time, the letter \"A\" appears in position {first_a + 1}.")
print(f" – And o last time, the letter \"A\" appeared in position {last_a + 1}.")
