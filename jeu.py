import random

secret = random.randint(1, 100)
essais = 0
choix = 0

print("J'ai choisi un nombre entre 1 et 100. Tu as 10 essais !")

while choix != secret and essais < 10:
    choix = int(input("Ton choix : "))
    essais = essais + 1

    if choix < secret:
        print("Plus grand !")
    elif choix > secret:
        print("Plus petit !")

if choix == secret:
    print("Bravo, tu as trouvé en", essais, "essais !")
else:
    print("Perdu ! Le nombre était", secret)
