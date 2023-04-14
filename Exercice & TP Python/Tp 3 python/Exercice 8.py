

"""

Exercice 8 :

L’élève placé au fond de la classe, près du radiateur, est le meilleur de la classe. Pour tuer le temps,
il décide de plier une feuille en deux puis en deux, puis… en deux, puis… Écrivez un algorithme
qui calcule l’épaisseur du pliage final à partir du nombre de plis et de l’épaisseur initiale de la
feuille.

"""


n=int(input( " nombre de pli"))
Ep=float(input(" epaisseur de la feuille"))

for loop in range(n):
    
 #Ep=0.1
 #Ep=0.1*2**n
 Ep*=2    #epaisseur de la feuille

print(Ep)

print(" l'epaisseur de la feuille est ", Ep)