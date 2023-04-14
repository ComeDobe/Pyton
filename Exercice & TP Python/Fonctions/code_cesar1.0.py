

from cgitb import text
from typing import Text

print("1- saisir 1 pour selectionner le cryptage : ")
print("")
print("2- saisir 2 pour selectionner le decryptage : ")
print("")

choice=int(input(" saisir votre choix : "))

    # cryptage
    
if choice==1: 
    boucle="2" 
    while boucle=="2":

        print(" vous avez choisi le cryptage")
    
        mot = input(" saisir un mot  : ")
        clef = int(input(" rentrez votre clef : "))
    
        message = [(ord(i)+clef) for i in mot]
        code_cesar = [chr(i) for i in message]
        mot_coder = "".join(code_cesar)
        print(mot_coder)
        boucle =input(" Souhaitez vous sortir de la boucle ? 1. oui   2. non ? ")
        # input("Appuyer sur Entrer pour continuer.")
    
    # Decryptage  
    
if choice==2: 
    boucle="2" 
    while boucle=="2":
        
        print(" vous avez choisi le decryptage")
        
        mot = input(" saisir un mot  : ")
        clef = int(input(" rentrez votre clef : "))

        message = [(ord(i)-clef) for i in mot]
        code_cesar = [chr(i) for i in message]
        mot_decoder = "".join(code_cesar)
        print(mot_decoder)
        boucle = input(" Souhaitez vous sortir de la boucle ? 1. oui   2. non ? ")
        # input("Appuyer sur Entrer pour continuer.")
        
