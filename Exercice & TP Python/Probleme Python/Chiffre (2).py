

 
	

# A partir du module standard random.py, on importe la fonction randint.
# Cette fonction permet de calculer une valeur pseudo-aléatoire.
from random import randint

# On demande une valeur pseudo-aléatoire entre 1 et 10 compris.

while True:
    
    valeur = randint(1, 10)
 
    chiffre = int(input("Veuillez saisir un entier : "))

    if chiffre == valeur:
     print("Trop fort, vous avez gagné :-)")
    else:
     print("Désolé, ce n'est pas la bonne valeur :-(")
    print("Il fallait trouver", valeur)