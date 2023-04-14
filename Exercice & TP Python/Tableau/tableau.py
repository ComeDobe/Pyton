

from tkinter import Menu


subjects = ["Français","Math","Géometrie","Informatique", 'art', 'plastique']
#subject_menu_item=["f'afficher la  note de {subjects}" for subject in subject] 

notes = []
total = 0
menu= [ " quitter ", "afficher les notes "] + subjects + [ " calcul la moyenne"]
for subject in subjects :
    note = int(input(f"Veuillez saisir la note de {subject} : "))
    total += note

moyenne = total / len(subjects)
print(f"La moyenne est de {moyenne}/20")


for i in range (0, len (menu)):
    print(f"{i}.menu[i]")
    
    choice = 9999
    while choice!=0:
        choice=int(input("votre choix : "));
        if choice == 1:
            for i in range(0, len(notes)):
                print( f"note de {subject[i]}: {note[i]}/20 ")
                
        elif choice >=2 and choice <=len(menu-2):
            print(f"note de {subject[choice]}: {note[choice]}/20 ")
            
        elif choice == menu[len(menu)-1]:
            
            print(f"La moyenne est de {moyenne}/20")
        


"""
subjects = ["Français","Math","Géometrie","Informatique"]
notes = [] #[0]*5
total = 0

#Valeur
for subject in subjects :
    note = int(input(f"Veuillez saisir la note de {subject} : "))
    total += note

moyenne = total / len(subjects)
print(f"La moyenne est de {moyenne}/20")
"""