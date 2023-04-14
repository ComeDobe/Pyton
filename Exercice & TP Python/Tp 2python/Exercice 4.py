


"""

Exercice 4 :

Ce jeu se passe entre deux joueurs. Ils montrent en même temps une main qui désigne un certain
nombre. Le gagnant se détermine par la procédure suivante :
— prendre connaissance du nombre de doigts de A,
— prendre connaissance du nombre de doigts de B,
— calculer la somme de ces deux nombres,
— si la somme est paire, A est le gagnant,
— si la somme est impaire, B est le gagnant.
Pour déterminer si un nombre est pair ou impair, il suffit de calculer le reste de la division par 2
(modulo 2) ; il vaut 0 dans le premier cas et 1 dans le second.

"""


A=int(input(" nombre de doigts de A :"))
B=int(input(" nombre de doigts de B :"))

if A<=1:
    print(" le joueur A à tirer ", A)
if A>=1:
 print("le joueur A à tirer ", A)

if B<=1:
    print(" le joueur Bà tirer ", B)
if B>=1:
 print("le joueur B à tirer ", B)

S=A+B
print(" la sommee de S est", S)

if (S%2)==0:
    print(" A est gagnant ")

else:
    print(" B est gagnat ")