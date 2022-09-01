from pathlib import Path

fichierInvalide = "C:/Users/Geoffrey/desktop/machinlearning/pythonGestionErreurs/fichier_invalide.abc"
readme = "C:/Users/Geoffrey/desktop/machinlearning/pythonGestionErreurs/readme.txt"

# ----------------------------------------------------------------------------------------------------------------------

# Attention faire cet encadré c'est pas mauvais mais c'est écrire du code alors que la gestion des erreurs avec moins de ligne
# pourrait le faire
# disons qu'ici on cadre le choix
# et entre parenthèse j'ai du changer le nom de fichier_invalid (sans e) car le fichier vide ne me retournait pas d'erreur !!!!

# while True:
#     choix = input("Quel fichier voulez-vous ouvrir ?\n readme.txt -> 1\n fichier_invalid.abc -> 2")
#     if choix != "1" and choix != "2":
#         print("c'est 1 ou 2 et rien d'autre, connard")
#         continue
#     else:
#         break


# if choix == "1":
#     choix = readme
# else:
#     choix = "fichierInvalid"
# -----------------------------------------------------------------------------------------------------------------------------

choix = input("Quel fichier voulez-vous ouvrir ?")
chemin = "C:/Users/Geoffrey/desktop/machinlearning/pythonGestionErreurs/"
choix = chemin+choix
# print(choix)

try:
    with open(choix, "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print("Erreur : le fichier est introuvable !")
except UnicodeDecodeError:
    print("Impossible d'ouvrir le fichier!")

# --------------------------------------------------------------------------------------------------

# on aurait pu l'écrire comme ceci -> attention de pas oublier de le fermer !!!

# try:
#     f = open(choix, "r")
#     print(f.read())
# except FileNotFoundError:
#     print("Le fichier est introuvable.")
# except UnicodeDecodeError:
#     print("Impossible d'ouvrir le fichier.")
# else:
#     f.close()

