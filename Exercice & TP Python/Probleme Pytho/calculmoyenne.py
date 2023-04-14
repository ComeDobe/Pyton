
matieres=[]
notes=[]

while True: 
    print("-")
    print("1- creation des matieres/saisie des notes.")
    print("2- suppression des matieres.")
    print("3- gestion des matieres/calcul de la moyenne.")
    print("4- quitter")
    
    choice = input("saisir votre choix: ")
    choice = choice.strip()

    if choice=="1":
        while True:
            print("-")
            matiere=(input("saisir la matiere? "))
            if matiere=="retour":
                break
            else:
                matieres.append(matiere)
            try: 
                note=int(input(f"saisir la note de {matiere}? "))
                notes.append(note)
                print("saisir retour pour sortir ")
                
            except ValueError:
                print("Resaisir la matiere.")

    elif choice=="2": 
        print("suppression")
        while True:    
            
            for (index,matiere) in enumerate (matieres):
                print(f"Pour supprimer la note de  {matiere}, saisir {index}.")
            suppression=input("")

            if suppression=="retour":
                break                
            elif int(suppression)>=0 and int(suppression)<len(matieres):
                matieres.pop(int(suppression))
                notes.pop(int(suppression))
            else: 
                print("-")
    elif choice=="3": 
        break
    elif choice=="4":
        break
    else:
        print("choix incorete reessayez?:")
while True:
    if choice=="4": 
        break
    try: 
        print("-")
        for (index, matiere) in enumerate (matieres): 
            print(f"saisir {index} pour afficher la note de {matiere}")
            
        print(f"saisir {len(matieres)} pour afficher toutes les notes")
        print(f"saisir {len(matieres)+1} pour afficher la moyenne generale")
        print(f"saisir {len(matieres)+2} pour sortir de la session")

        choice=int(input()) 

        if choice>=0 and choice<len(matieres): 
            print("-")
            print(f"Votre note en {matieres[choice]} est de {notes[choice]}/20.")

        elif choice==(len(matieres)): 
            print("-")
            for (index, matiere) in enumerate(matieres):
                print(f"Votre moyenne en {matiere} est de {notes[index]}/20 ")

        elif choice==((len(matieres))+1): 
            total=sum(notes)
            moyenne=total/(len(notes))
            print("-")
            print(f"la moyenne générale est de {moyenne}/20.")

        elif choice==((len(matieres))+2): 
            break
        else:
            print("-")
            print("Reessayez, la saisie est incorete: ")
    except ValueError:
           print("-")
       