
from random import*


print(" jeux de tirage au hasard")

while True:

  prix= randint(1,10)
    
  choix= int (input(" saisir un prix")) 
    
    
  if  choix>0 and choix <=10:
    
     print(" vous etes dans l'intervalle de choix")
     
  else:
        print(" intervalle non defini") 
        
        quit()
    
  if choix<prix:
        
        print(" c'est plus il faut continuer la saisie")
        
  if choix>prix:
        
        print( " c'est moins continuer de saisir")
  else:
            
      print(" bravo! vous avez gagné")
    
    
    
    
    