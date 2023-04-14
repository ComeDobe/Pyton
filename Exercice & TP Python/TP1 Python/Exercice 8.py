#   Exercice N 8

# Saisissez le prix unitaire HT d’un produit et la quantité commandée. Calculez le montant HT de la commande, appliquez une remise de 15% et calculez le prix TTC après avoir saisi le taux de TVA.


ht=float(input(" prix ht"))
Q=int(input("saisir la quantité des produits:"))
Mht=Q*ht
print("le montant ht", "est", Mht)
R=Mht*15/100
x=Mht-R
print("le prix avant tva est", x)
tva=float(input(" saisir la tva:"))
a=Mht*tva/100
ttc=x+a
print("le prix ttc apres tva est ", ttc)