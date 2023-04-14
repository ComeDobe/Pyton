print("resolution de ax^2 + bx + c = 0 :")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if (a != 0):
    discr = b*b - 4*a*c
    if (discr > 0):
        x1 = (b*b - discr**(1/2))/(-2*a)
        x2 = (b*b + discr**(1/2))/(-2*a)
        print("Les solutions sont", x1, "et", x2)
    if (discr == 0):
        x = -b/a
        print("La solution est", x)
    if (discr < 0):
        print("Pas de solution réelle")
else:
    if (b != 0):
        print("La solution est", -c/b)
    else:
        if (c == 0):
            print("Tout réel est solution.")
        else:
            print("Aucune solution.")