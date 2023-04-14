

from ast import Break

imm=input( " immatricule chef de famille O/N?")
charge=input( " enfant à charge O/N?")
Age=int(input(" age de l'enfant à la fin du mois"))
NBHT=float(input(" nombre d'heure à la fin du mois: "))

M="mensualité"
AF1 = 120.60
AF2 = 180.90
AF3 = 217.00
AF4 = 253.20

if Age < 3:
     mensualité = (AF1/145)*85
     print( " Alloc fam1", mensualité)
   
if Age>= 3 and Age<= 6:
    mensualité = (AF2/145)*85

    print(" Alloc fam2", mensualité)

elif Age< 10 and Age> 6:
    mensualité = (AF3/145)*85
    print(" Alloc fam3", mensualité)

if Age < 21 and Age >= 10:
    mensualité = (AF4/145)*85

    print(" Alloc fam4", mensualité)

if NBHT>=145:
    print("il sera versé une mensualité entiere de ", mensualité)

elif NBHT<144 and NBHT>75:
    
    print(" la mensualité est proratisé", mensualité)


else:
     print(" pas d'indemnité")