


print("conversion d'une valeur en cm/pouce")
print(" 1- choisir la conversion en centimetre")
print(" 2- choisir la conversion en pouce")

while True: 

 choice = input(" votre choix 1 ou 2?")
 
 if choice =="1":      
    boucle = "2"
# while boucle == "2":
    valeur_pouce=float(input("saisir la valeur en pouce"))
    valeur_cm = round(float(valeur_pouce*2.54))
    print(f" la valeur en pouce est ", valeur_pouce,  " convertie en ", valeur_cm, " cm")
    
    boucle=input(" voulez vous rester dans le programme o/n ?")

 if choice == "2":
  boucle = "2"
# while boucle == "2":
 valeur_cm=float(input("saisir la valeur en cm"))
 valeur_pouce = round(float(valeur_cm*0.39))
 print(f" la valeur en pouce est ", valeur_cm, " convertie en ", valeur_pouce, " pouce")
    
 boucle=input(" voulez vous rester dans le  programme o/n ?")
    
 break