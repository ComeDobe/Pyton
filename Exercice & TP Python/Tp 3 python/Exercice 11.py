

"""

Exercice 11 :

Réécrire l’algorithme précédent, mais cette fois-ci on ne connaît pas d’avance combien l’utilisateur
souhaite saisir de nombres. La saisie des nombres s’arrête lorsque l’utilisateur entre un zéro.

"""


a =  int(input('saisir un chiffre'))
 
if a==0 :
     print(" action non autorisée")
     
     quit()

b=  int(input('saisir un chiffre'))
 
if b==0: 
     print(" action non autorisée")
     quit()
     
c =  int(input('saisir un chiffre'))
if c==0:
        print(" action non autorisée")
        quit()

print("le plus grand des chiffres est", max(a,b,c))
   