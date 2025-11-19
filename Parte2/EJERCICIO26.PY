

import random

print("Lanzando tres dados...")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)

print(f"Resultados: {dado1}, {dado2}, {dado3}")

seises = 0
if dado1 == 6: seises += 1
if dado2 == 6: seises += 1
if dado3 == 6: seises += 1

if seises == 3:
    print("Excelente")
elif seises == 2:
    print("Muy bien")
elif seises == 1:
    print("Regular")
else:
    print("Pésimo")