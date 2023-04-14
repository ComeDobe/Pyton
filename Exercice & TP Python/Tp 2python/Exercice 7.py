

"""

Exercice 7 :
Saisissez un montant TTC et appliquez une remise avec les conditions suivantes :
— si le montant est compris entre 500 € et 1 000 €, le taux de remise est de 2 %,
— si le montant est compris entre 1 000 € et 2 000 €, le taux de remise est de 5 %,
— si le montant est supérieur à 2 000 €, le taux de remise est de 10 %.

"""

A=int(input(" saisir le montant TTC :"))

if( A>2000):
 
 print( " on a une remise de 10% ", A*(1-0.1))
   
elif A>1000 and A<2000:

  
 print( " on a une remise de 5% ", A*(1-0.05)) 

elif A>500 and A<1000:
  

 print( " on a une remise de 2% ",  A*(1-0.02))
