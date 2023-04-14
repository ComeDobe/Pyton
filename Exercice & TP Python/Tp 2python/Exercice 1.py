


"""

Exercice 1 :

Calculez la moyenne des notes d’un élève après avoir saisi les notes de français, de math, de
géométrie et d’informatique. Il faut tenir compte de coefficients de pondération par matière qui
seront saisis eux aussi.

"""




x1=float(input("saisir la note des Maths :"))
A1=float(input(" saisir le coefficient de matht :"))
x2=x1*A1
print(" la note*le coeff de M est", x2)

y1=float(input("saisir la note de Francais :"))
B1=float(input(" le coeff de Francais "))
y2=y1*B1
print( " la note*le coeff de F est ", y2)

z1=float(input("saisir la note de Geometrie :"))
C1=float(input("le coeff de Geometrie "))
z2=z1*C1
print( " la note*lecoeff de G est ", z2)

h1=float(input("saisir la note d'informatique: "))
D1=float(input(" le coeff d'info est"))
h2=h1*D1
print( " la note*lecoeff de l'info est ", h2)


moyenne= (h2+z2+y2+x2 )/(D1+B1+C1+A1)

print("la moyenne generale est ", moyenne)