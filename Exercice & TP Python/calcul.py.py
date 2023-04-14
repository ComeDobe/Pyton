
  # Mon premier programme en python

                          # exercice N 1

# À partir de deux nombre a et b, écrire le résultat pour l’addition, la soustraction, la division et la multiplication.


 # Addition 


 #a = int(input("saisir un nombre a: "))
 #b =  int(input("saisir un nombre b: "))
 #somme = a+b
 #print(" la somme de", a, "et", b, "vaut", somme)

  # division    

  # a = int(input("saisir un nombre a: "))
  # b =  int(input("saisir un nombre b: "))
  # div= a/b
  # print("le quotien de", a, "et", b, "vaut", div)



  # soustraction 
  

  #a = int(input("saisir un nombre a: "))
  #b =  int(input("saisir un nombre b: "))
  #difference = a-b
  #print(" la difference de", a, "et", b, "vaut", difference)


 # multiplication



 # a = int(input("saisir un nombre a: "))
 # b =  int(input("saisir un nombre b: "))
 # mult = a*b
 # print(" la mult de", a, "et", b, "vaut", mult)

                       #  Exercice N 2

# Écrire un algorithme permettant d’afficher le double d’un nombre x.


 # x = int(input("saisir la valeur de x: "))
 # Double = 2*x
 # print(" le Double de ", x, "vaut", Double)


                         #  Exercice N 3

                  
# Écrire un algorithme permettant de calculer l’aire d’un carré de côté x. 

 # x = int(input("saisir la valeur de x: "))
 # aire=x**2
 # print(" l'aire de ", x, "vaut", aire)
     
     
                        # Exercice N 4

# Écrire un algorithme qui affiche « Hello prénom » où prénom est une valeur saisie par l’utilisateur.

 # prenom = input("hello prenom: ")
 # print(" ton prenom est", prenom)
   

                          # Exercice N 5

# Écrire un algorithme permettant de calculer l’âge d’une personne à partir de son année de naissance  saisie au clavier.   


 #a = int(input("saisir une année a: "))
 #b =  int(input("saisis ton année de naissance b: "))
 #Age  = a-b
 #print(" ton Age en", a, "est", Age, "ans")
 
                    #  Exercice N 6

# Écrire un algorithme qui calcul le prix TTC à partir d’un prix HT et d’une TVA de 20 % (prestation de service en France).
              
 # ht= int(input("saisir le prix  ht: "))
 # tva =  int(input("saisir la valeur du tva: "))
 # ttc = ht*(1+0.2)
 # print(" le prix ttc de ", ht,"euro", "est", ttc, "euro")

                       
                    #    Exercice N 7


# Calculez le volume d’un parallélépipède dont la largeur, la longueur et la hauteur seront saisies au clavier.


# L=int(input("saisir la longueur:"))
# l=int(input("saisir la largeur:"))
# h=int(input("saisir la hauteur:"))
# v=L*l*h
# print("le volume du parallelepipede", "est", v)


                  #   Exercice N 8

# Saisissez le prix unitaire HT d’un produit et la quantité commandée. Calculez le montant HT de la commande, appliquez une remise de 15% et calculez le prix TTC après avoir saisi le taux de TVA.


# ht=float(input(" prix ht"))
# Q=int(input("saisir la quantité des produits:"))
# Mht=Q*ht
# print("le montant ht", "est", Mht)
# R=Mht*15/100
# x=Mht-R
# print("le prix avant tva est", x)
# tva=float(input(" saisir la tva:"))
# a=Mht*tva/100
# ttc=x+a
# print("le prix ttc apres tva est ", ttc)


                             #  Exercice N 9

                    
# Calculez la moyenne des notes d’un élève après avoir saisi les notes de français, de math, de géométrie et d’informatique.


# A=int(input("saisir la note des Maths :"))
# B=int(input("saisir la note de Francais :"))
# C=int(input("saisir la note de Geometrie :"))
# D=int(input("saisir la note d'informatique: "))
# Moyenne=(A+B+C+D)/4
# print("la moyenne est de", Moyenne)


                              #  Exercice N 10


# Affichez une table de multiplication (jusqu’à 10) dont l’ordre (le nombre concerné) sera saisi au clavier.



n=int(input("saisissez une table:"))
print("la table de multiplication de n est  egale à : ")
for i in range ( 1, 10 ):

 print(i, "x", n , "=", i*n)
     
