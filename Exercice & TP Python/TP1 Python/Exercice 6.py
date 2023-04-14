 #  Exercice N 6

# Écrire un algorithme qui calcul le prix TTC à partir d’un prix HT et d’une TVA de 20 % (prestation de service en France).
              
ht= int(input("saisir le prix  ht: "))
tva =  int(input("saisir la valeur du tva: "))
ttc = ht*(1+0.2)
print(" le prix ttc de ", ht,"euro", "est", ttc, "euro")