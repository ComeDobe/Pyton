

# Écrire l'algorithme qui demande à l'utilisateur le mot à chiffrer et la clef de chiffrage pour crypter le mot en César.


# # liste=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "z" ]
# liste=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for x in range(len(liste)):

#     liste.append(liste[x])
    

# def chiffrage_lettre(lettre,liste, clef):
    
#     for i in range(len(liste)):
#         if lettre== '':
#             return ''
#         elif liste[i]==lettre:
            
#             return  str(liste[i+clef])
        
#     return '?'
    
# message_chiffre=str()
    
    
            
# while True:   
     
#     message=input("saisir un message: ")

#     clef=int(input("saisir une clef entre 0 à 25: "))
    
#     for lettre in message:
#         message_chiffre += chiffrage_lettre(lettre, liste, clef)
#     print(message_chiffre)
    
    
    
    
    
#                 #  autre methode



from cgitb import text
from typing import Text

print("1- saisir 1 pour selectionner le cryptage")
print("2- saisir 2 pour selectionner le decryptage")
# vduprint("3- saisir 3 pour sortir de la session ")

choice=int(input(" saisir votre choix"))



    
while True:
    
    if choice==1:
        print("vous avez choisi le cryptage")
    
        mot = input(" saisir un mot  : ")
        clef = int(input("rentrez votre clef : "))
    
        message = [(ord(i)+clef) for i in mot]
        code_cesar = [chr(i) for i in message]
        mot_coder = "".join(code_cesar)
        print(mot_coder)
        
        break

    if choice==2:
        print(" vous avez choisi le decryptage")
        
        mot = input(" saisir un mot  : ")
        clef = int(input("rentrez votre clef : "))

        message = [(ord(i)-clef) for i in mot]
        print(" le decryptage est: ", message)
        code_cesar = [chr(i) for i in message]
        mot_decoder = "".join(code_cesar)
        print(mot_decoder)
        
    
  