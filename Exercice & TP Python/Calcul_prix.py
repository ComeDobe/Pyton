




prixpop=5 
prixmin=7
prixmaj=12

age=int(input("quel est votre?"))
pop= input("souhaitez du popcorne? o/n?")

if age<18 and pop=="o":
    
    prixtotal= prixmin+prixpop
     
    print("le prix total est de",prixtotal, "euro")
 
elif pop=="n":
    
    print(" tu dois payer",prixmin,"euro")
    
    quit()
    
elif age>18 and pop == "o" :
       
        prixtotal= prixmaj+prixpop
         
        print( "le prix total est",prixtotal,"euro")  
else:       
        
    print("le prix total est de",prixmaj,"euro")
    







