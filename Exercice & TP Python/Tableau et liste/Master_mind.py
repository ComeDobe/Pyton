
import random


num = random.randrange(1,99999) 
                      
n = int(input("devinez le nombre à 5 chiffre:"))
  
if(n == num):             
     print("Bien vous avez devinez le chiffre en seulement un essai!")
else:
   ctr = 0    
  
while(n!=num):
    
          ctr += 1             
                                  
          count = 0
  
          n = str(n) 
                                              
          num = str(num)
   
          correct=[]        
      
          for i in range(0,5): 
              
              if(n[i] == num[i]): 
                  
                  count += 1    
                  
                  correct.append(n[i])     
              else:
                  continue
  
          
          if (count < 5) and (count != 0):     
              print("pas tout à fait mais vous avez obtenu ",count," chiffre correct!")
              print("le chiffre dans le input .")
                
              for k in correct:
                  print(k, end=' ')
  
              print('\n')
              print('\n')
              n = int(input("Entrez le choix suivant "))
  
         
          elif(count == 0):         
              print("aucun chiffre ne correspond ")
              n=int(input("Entrez le choix suivant: ")) 
  
if n==num:                
         print("tu es devenu un mastermind!")
         print("il a fallu",ctr,"essai")