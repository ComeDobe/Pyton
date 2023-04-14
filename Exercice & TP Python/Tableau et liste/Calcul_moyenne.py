




"""
Calculez la moyenne des notes d’un élève après avoir saisi les notes de français, de math, de
géométrie et d’informatique.


Ensuite ajoutez un menu deroulant, liste des matieres

"""


from tkinter import Menu

while True:
 subjects = ["Français","Math","Géometrie","Informatique"]

 notes = []
 total = 0
 
 print("1- saisir les notes/calcul des moyennes")
 print("2- afficher les notes")
 print("3- afficher la moyenne")
 print("4- Quitter")
  
 choice = input("saisir votre choix: ")
  
 choice = choice.strip()
 

 for subject in subjects :
    note = int(input(f"Veuillez saisir la note de {subject} : "))
    total += note

 moyenne = total / len(subjects)
 print(f"La moyenne est de {moyenne}/20")


 for i in range (0, len (choice)):
    # print(f"{i}.choice[i]")
    
    choice = 9999
    while choice!=0:
        choice=int(input("votre choix : "));
        if choice == 1:
            for i in range(0, len(notes)):
                print( f"note de {subject[i]}: {note[i]}/20 ")
                
        elif choice ==2 and choice <=len(choice-2):
            print(f"note de {subject[choice]}: {note[choice]}/20 ")
            
        elif choice == choice[len(choice)-1]:
            
            print(f"La moyenne est de {moyenne}/20")
        


