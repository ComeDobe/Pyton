"""

Exercice 3 :

Saisissez un nombre compris entre 1 et 10. En cas d’erreur de saisie, il y a affichage d’un message «
Valeur non permise ». Si le nombre est égal au nombre magique connu du programme, il affiche «
Gagné » sinon il affiche un message « Trop petit » ou « Trop grand » suivant la valeur saisie.
(reprise de « Chiffre magique 1 » pour utiliser des boucles)

"""



from random import randint
from tkinter import E


while True:
    
    n = randint(1, 10)
 
    chiffre = int(input("Veuillez saisir un entier : "))
    
    if chiffre <=10 and chiffre>0:
        print(" valeur permise")
          
    else:
        
        print(" valeur non permise")
        quit()

    if chiffre <n:
          print(" c'est plus, veuillez saisir un autre chiffre")
      
    elif chiffre>n:
      print(" c'est moins, veuillez saisir un autre chiffre")
      
    else:
       break
     
         
if chiffre!=0:
        print(" bravo vous avez gagné")