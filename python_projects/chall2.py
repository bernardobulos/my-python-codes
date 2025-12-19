# Texto somente em inglês. 🇧🇷
# Text only in English. 🇺🇸
# Texto sólo en inglés. 🇪🇸
# Texte uniquement en anglais. 🇫🇷

# PRACTICAL CHALLENGE 2
# Suppose you are managing a sports competition and you have a list of tuples representing the teams' results in different events. Each tuple contains the team name, followed by a list of scores obtained in each round of the competition.
# 1. 1. Calculate the average score for each team and store these values ​​in a new list called "averages".
# 2. Sort the "averages" list in descending order.
# 3. Create a new list called "classification" that contains tuples, where each tuple contains the team name and its average score.
# 4. Display the final team rankings on the screen, showing the team name and average score, from the highest-scoring team to the lowest-scoring team.

from random import randint

teams = [
    ("Golden Tigers", [randint(1, 100), randint(1, 100), randint(1, 100)]),
    ("Crimson Lions", [randint(1, 100), randint(1, 100), randint(1, 100)]),
    ("Black Eagles", [randint(1, 100), randint(1, 100), randint(1, 100)]),
    ("Pink Panthers", [randint(1, 100), randint(1, 100), randint(1, 100)])
]
avarages = []
classification = []

for team, scores in teams:
    avarage = sum(scores) / len(scores)
    avarages.append(avarage)
    classification.append((team, avarage))
avarages.sort(reverse=True)
classification.sort(key=lambda x: x[1], reverse=True)

print("🏆 FINAL CLASSIFICATION 🏆")
for position, (team, avarage) in enumerate(classification, start=1):
    print(f"{position}º place — {team} ({avarage:.2f} pts)")
