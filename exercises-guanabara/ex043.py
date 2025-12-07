# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seus status, de acordo com a tabela seguinte: Abaixo de 18.5 = Abaixo do peso; Entre 18.5 e 24.9 = Peso Ideal; 25 até 29.9 = Sobrepeso; 30 até 40 = Obesidade; e acima de 40 = Obsesidade Mórbida. 🇧🇷
# Develop a logic that reads a person's weight and height, calculates their BMI, and displays their status according to the following table: Below 18.5 = Underweight; Between 18.5 and 24.9 = Ideal Weight; 25 to 29.9 = Overweight; 30 to 40 = Obesity; and above 40 = Morbid Obesity. 🇺🇸
# Desarrollar una lógica que lea el peso y la altura de una persona, calcule su IMC y muestre su estado de acuerdo con la siguiente tabla: Menos de 18,5 = Bajo peso; Entre 18,5 y 24,9 = Peso ideal; 25 a 29,9 = Sobrepeso; 30 a 40 = Obesidad; y más de 40 = Obesidad mórbida. 🇪🇸
# Élaborez un système logique qui lit le poids et la taille d'une personne, calcule son IMC et affiche son statut selon le tableau suivant : Moins de 18,5 = Insuffisance pondérale ; Entre 18,5 et 24,9 = Poids idéal ; De 25 à 29,9 = Surpoids ; De 30 à 40 = Obésité ; et plus de 40 = Obésité morbide. 🇫🇷

height = float(input("Enter a person's height (in meters): "))
weight = float(input("Enter a person's weight (in kilograms): "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"This person ({height:.2f} m tall and weighing {weight:.2f} kg) is underweight.")
    print(f"Your BMI is {bmi:.1f}.")
elif 18.5 <= bmi < 25:
    rint(f"This person ({height:.2f} m tall and weighing {weight:.2f} kg) is their ideal weight.")
    print(f"Your BMI is {bmi:.1f}.")
elif 25 <= bmi < 30:
    print(f"This person ({height:.2f} m tall and weighing {weight:.2f} kg) is overweight.")
    print(f"Your BMI is {bmi:.1f}.")
elif 30 <= bmi <= 40:
    print(f"This person ({height:.2f} m tall and weighing {weight:.2f} kg) is obese.")
    print(f"Your BMI is {bmi:.1f}.")
else:
    print(f"This person ({height:.2f} m tall and weighing {weight:.2f} kg) is morbidly obese.")
    print(f"Your BMI is {bmi:.1f}.")
