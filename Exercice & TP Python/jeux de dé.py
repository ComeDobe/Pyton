from random import randint 
 
compteur = [0 for i in range(6)]
 
 
for i in range(6):
    # je tire un dé
    de = randint(1, 6)
    
    compteur[de - 1] += 1
 
for i in range(1, 6) : 
   
    print("Le chiffre {} est apparu {} fois".format(i, compteur[i - 1]))
    