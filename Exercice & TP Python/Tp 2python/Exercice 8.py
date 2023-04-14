
"""

Exercice 8 :
Cherchons à résoudre l’équation « ax + b = 0 ».
Pour cela, saisissons les deux nombres a et b et affichons le résultat correspondant.
Si a = 0 et b = 0 alors l’ensemble des solutions est l’ensemble R.
Si a = 0 et b!= 0 alors l’ensemble des solutions est l’ensemble vide.
Si a!= 0 alors la solution est (-b / a).

"""


print(" resolution de l'equation ax+b=0 ")
a=int(input(" saisir la valeur de a "))
b=int(input("saisir la valeur de b: "))
  
x=-b/a

if ( a!=0):
    print( " l'equation admet une solution dans le reel", -b/a)

else:

 if (b==0 ):
    print(" tout reel est solution de l'equation")

 else:     

  print(" l'equation n'admet pas de solution reel")