
"""


Exercice 6 :
Saisissez le prix HT d’un produit. Affichez les taux de TVA possibles ainsi qu’un code :
Pour une TVA de 5,5 %, saisissez 1
Pour une TVA de 19,6 %, saisissez 2
Pour une TVA de 33 %, saisissez 3
L’utilisateur saisit un code (1, 2 ou 3). Calculez le prix TTC et affichez un message : « Le prix HT
est de 100 €, la TVA est de 19,6 % et le prix TTC est de 119,60 €. »

"""



HT=float(input(" saisir le prix ht du produit :"))

code1=5.5
code2=19.6
code3=33

code = 1 or 2 or 3
code=int(input(" saisir le code de la tva "))

if code==1:
    tva=HT*0.055
    ttc=HT+tva
    print( " le prix  HT est " , HT , "et le prix ttc est  ", ttc )
    


if code==2:
    tva=HT*0.196
    ttc=HT+tva
    print( " le prix ht est ", HT,  "et le prix ttc est  ", ttc )
   
if code==3:
    tva=HT*0.33
    ttc=HT+tva
    print( " le prix ht est  ", HT, "et le prix ttc est  ", ttc )
   