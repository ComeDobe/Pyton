
"""

Exercice 2 :

Saisir trois nombres et afficher un message indiquant s’ils sont triés en ordre croissant ou non.
"""



print(" on effectue le tri des nombres suivant : ")
a=int(input(" saisir le premier nombre  "))
b=int(input(" saisir le deuxieme nombre  "))
c=int(input(" saisir le troisieme nombre  "))

print( " le tri en ordre croissant est :")
nombres= [ a,b ,c ]
nombres.sort()
print(nombres)

print( "tri decroissant ")

nombres.sort( reverse=True)
print(nombres)
