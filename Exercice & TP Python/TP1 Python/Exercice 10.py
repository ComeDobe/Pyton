#  Exercice N 10


# Affichez une table de multiplication (jusqu’à 10) dont l’ordre (le nombre concerné) sera saisi au clavier.



n=int(input("saisissez une table:"))
print("la table de multiplication de n est  egale à : ")
for i in range ( 1, 10 ):

 print(i, "x", n , "=", i*n)
     
