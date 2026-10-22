import random

secret = random.randint(1, 100)
essais = 0

while True:
    saisie = input("Ton nombre (1 à 100)?")
    try:
        nombre = int(saisie)
    except ValueError:
        print("Ce n'est pas un nombre")
        continue
    essais += 1
    if nombre < secret:
        print("Plus grand")
    elif nombre > secret:
        print("Plus petit")
    else:
        print(f"Trouvé en {essais} essai(s)")
        break