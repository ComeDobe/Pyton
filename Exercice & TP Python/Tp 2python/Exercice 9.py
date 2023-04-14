

"""

Exercice 9 :

Saisissez les notes d’un élève pour les matières suivantes : français, mathématiques, géographie et
informatique.
Si la moyenne est comprise entre 16 et 20, la mention est « Très bien ».
Si la moyenne est comprise entre 12 et 16, la mention est « Bien ».
Si la moyenne est comprise entre 8 et 12, la mention est « Assez bien ».
Si la moyenne est comprise entre 4 et 8, la mention est « Insuffisant ».
Si la moyenne est comprise entre 0 et 4, la mention est « Nul ».

"""
 
print( " calcul de la moyenne :")
var0=int(input("saisir la note des Maths :"))
var1=int(input("saisir la note de Francais :"))
var2=int(input("saisir la note de Geographie :"))
var3=int(input("saisir la note d'informatique: "))

a=(var0+var1+var2+var3)/4
print ( " la moyenne est: ", (var0+var1+var2+var3)/4 )

if (a<4):

 print(" la mentionne est nulle " )

elif a>4 and a<8:

    print(" la mention est insuffisante:")

elif a>8 and a<12:
    print(" la mention est assez bien :")


elif a>12 and a<16:
    print( " la mention est bien: ")
else:
    print(" la mention est tres bien: ")
