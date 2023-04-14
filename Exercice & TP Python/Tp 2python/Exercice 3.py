


""""

Exercice 3 :

Tous les enfants qui ont moins de 3 ans doivent recevoir une palette de petits pots. Saisissez l’année
de naissance et calculez si le bébé a gagné une palette ou pas.

"""

a = int(input("saisir une année : "))
b =  int(input("saisis ton année de naissance : "))
Age  = a-b
print(" ton Age en", a, "est", Age, "ans")

if ( Age<3 ):
 print(" tu recois une palette de pot: ")

else:
 print(" tu es trop agé")
