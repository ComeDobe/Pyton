

"""

Exercice 10 :

Écrire un algorithme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite
quel était le plus grand parmi ces 20 nombres.
SANS TABLEAUX !!!

"""

n=20
chiffre=0
 
for i in range(0,n):
    
 n =  int(input('saisir un chiffre')) 
 
 if n>chiffre:
     chiffre=n


print(" le plus grand des chiffres est ", chiffre)
