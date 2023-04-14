
"""
Exercice 1 :

Réalisez un jeu de dés utilisant les aiguillages conditionnels. Au démarrage du programme, il
calcule au hasard un nombre entre 1 à 6 (utilisez la fonction suivante : valeur <— HASARD(valeur
mini , valeur maxi)). Le programme affiche « Vous avez fait un six » et il affiche la face du dé, sur 3
lignes, par exemple :
«0 0»
« 0 »
«0 0»

"""

from random import randint

d = randint(1,6)

print("Vous avez fait",d)

if d == 1 :
    print("┌───┐")
    print("| • |")
    print("└───┘")

elif d == 2 :
    print("┌───┐")
    print("|• •|")
    print("└───┘")

elif d == 3 :
    print("┌•────┐")
    print("|  •  |")
    print("└────•┘")

elif d == 4 :
    print("┌•───•┐")
    print("|     |")
    print("└•───•┘")

elif d == 5 :
    print("┌•───•┐")
    print("|  •  |")
    print("└•───•┘")

elif d == 6 :
    print("┌•───•┐")
    print("|•   •|")
    print("└•───•┘")