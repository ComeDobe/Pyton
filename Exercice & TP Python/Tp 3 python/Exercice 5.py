
"""

Exercice 5 :

On se propose de calculer la moyenne des notes d’un élève pour certaines matières ; français,
maths, géographie et informatique.
Pour chacune de ces matières, il faudra saisir un coefficient de pondération compris entre 1 et 10.
Calculez la moyenne en tenant compte des coefficients de pondération.
Affichez une appréciation :
Si la moyenne est comprise entre 16 et 20, la mention est « Très bien ».
Si la moyenne est comprise entre 12 et 16, la mention est « Bien ».
Si la moyenne est comprise entre 8 et 12, la mention est « Assez bien ».
Si la moyenne est comprise entre 4 et 8, la mention est « Insuffisant ».
Si la moyenne est comprise entre 0 et 4, la mention est « Nul ».
Il faut contrôler que les notes sont comprises entre 0 et 20 et que les coefficients sont compris
entre 1 et 10. (reprise de l’exercice 9 feuille niveau II pour utiliser des boucles)
"""


print( " calcul de la moyenne :")


var0=int(input("saisir la note des Maths :"))

if var0<=20 and var0>0:
      print(" on peut continuer le calcul de la moyenne")
else:
    print(" veuillez rester dans lintervalle defini")

e=float(input(" le coeff de maths"))
if e<=10 and e>0:
      print(" on peut continuer le calcul de la moyenne")
else:
    print(" veuillez rester dans lintervalle defini")
A=var0*e

print(" la note*coef de M est ", A)

var1=int(input("saisir la note de Francais :"))

if var1<=10 and var1>0:
      print(" on peut continuer le calcul de la moyenne")
else:
    print(" veuillez rester dans lintervalle defini")
    
b=float(input(" le coeff de Francais "))

if b<=10 and b>0:
      print(" on peut continuer le calcul de la moyenne")
else:
    print(" veuillez rester dans lintervalle defini")
B=var1*b

print(" la note*coef de F est ", B)

var2=int(input("saisir la note de Geographie :"))

if var2<=20 and var2>0:
      print(" on peut continuer le calcul de la moyenne")
else:
    print(" veuillez rester dans lintervalle defini")
c=float(input(" le coeff de geographie est  "))
if c<=10 and c>0:
      print(" on peut continuer le calcul de la moyenne")
else:
    print(" veuillez rester dans lintervalle defini")

C=var2*c
print(" la note*coef de G est ",C)

var3=int(input("saisir la note d'informatique: "))

if var3<=20 and var3>0:
      print(" on peut continuer le calcul de la moyenne")
else:
    print(" veuillez rester dans lintervalle defini")
d=float(input(" le coeff d'informatique "))
if d<=10 and d>0:
      print(" on peut continuer le calcul de la moyenne")
else:
    print(" veuillez rester dans lintervalle defini")

D=var3*d
print(" la note*coef de I est ", D)

a=(A+B+C+D)/(e+b+c+d)
print ( " la moyenne est: ",(A+B+C+D)/ (e+b+c+d) )

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
