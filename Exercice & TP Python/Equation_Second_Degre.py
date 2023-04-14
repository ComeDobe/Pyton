


import math


print("Equation du second degré de la forme ax**2+bx+c=0 : ")

a=int(input(" saisir la valeur de a : "))
b=int(input(" saisir la valeur de b : "))
c=int(input(" saisir la valeur de c : "))



discr = b*b-4*a*c
print(" le dicriminant est :", discr)


if discr > 0:
    x1=(-b-discr**0.5)/(2*a)
    x2=(-b+discr**0.5)/(2*a)
    print("l'equation admet deux solutions", x1 , x2 )
    
elif discr == 0:
    x0 = -b/2*a
    print( " l'equation admet une solution double",x0 )
    
elif discr <0:
    print(" l'equation n'admet pas de solution reelle")
    
else:
    if (b != 0):
        print("La solution est", -c/b)
    else:
        if (c == 0):
            print("Tout réel est solution.")
        else:
            print("Aucune solution.")
     