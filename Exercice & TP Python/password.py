

password="bonjour"

userpassword=input(" saisir le mp")

attempt=3

while userpassword!=password  and attempt!=0:
      password=input(f" saisir un mp il vous reste {attempt},  tentative")

attempt=attempt-1
attempt==2

if attempt==0:
    rep=input(" voulez vous repondre à la question /o")=="o"
    if rep: #pareil que rep = true
        repsecret=input(" le nom de votre animal de compagnie").lower()=="minou"  # lower conversion en minucule
        if repsecret!="minou":
         print(" compte bloqué")
        else:
          print(" authentification reussi ")

    else: 
        print(" compte bloqué")
else:
            
        print(" accés reussi")
        
        quit()
        