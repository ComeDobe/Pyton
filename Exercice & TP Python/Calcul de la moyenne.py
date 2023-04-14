

matieres=[]
notes=[]


print("Pour commencer, créez des matières et insérez-y votre moyenne. ")


while True: 
    print("-")
    
    print("Pour créer de nouvelles matières, entrez new.")
    print("Pour supprimer des matières, entrez <<Supprimer>>.")
    print("Pour passer à la consultation des notes, entrez cons.")
    print("Pour quitter le programme complètement, entrez quit")
    
    choix1=int(input())

    if choix1==1: 
    
        while True:
            print("-")
            print("Pour arrêter de créer de nouvelles matières et revenir au menu précédent, entrez <<Retour>>.")
            nouvelleMatiere=(input("Quel est le nom de la matière à créer? "))
            if nouvelleMatiere=="retour":
                break
            else:
                matieres.append(nouvelleMatiere)
            
            try:
                nouvelleNote=int(input(f"Combien avez-vous obtenu en {nouvelleMatiere}? "))
                notes.append(nouvelleNote)
            except ValueError:
                print("Note invalide. Matière non créée.")
                matieres.pop(-1)

    elif choix1=="supprimer": 
        print("---Suppression---")
        while True:    
            
            for (index,matiere) in enumerate (matieres):
                print(f"Pour supprimer votre moyenne en {matiere}, entrez {index}.")
            print("Pour sortir du menu suppression, entrez <<Retour>>")
            suppression=input("")

            if suppression=="retour":
                break                
            elif int(suppression)>=0 and int(suppression)<len(matieres):
                matieres.pop(int(suppression))
                notes.pop(int(suppression))
            else: 
                print("-")
                print("Je n'ai pas compris. Voulez-vous dire <<Retour>>? ")

            

    elif choix1=="consulter": 
        break
    
    elif choix1=="quitter":
        break

    else:
        print("Je n'ai pas compris votre choix. Rééssayez:")


while True:
    if choix1=="quitter": 
        break

    try:
        print("-")
        for (index, matiere) in enumerate (matieres): 
            print(f"Pour afficher la note de {matiere}, entrez {index}")
            

        print(f"Pour afficher toutes les notes ensemble, entrez {len(matieres)}") 
        print(f"Pour afficher la moyenne générale, entrez {len(matieres)+1}")
        print(f"Pour arrêter le programme, entrez {len(matieres)+2}")

        choix2=int(input()) 

        if choix2>=0 and choix2<len(matieres): 
            print("-")
            print(f"Votre note en {matieres[choix2]} est de {notes[choix2]}/20.")

        elif choix2==(len(matieres)):
            print("-")
            for (index, matiere) in enumerate(matieres):
                print(f"Votre moyenne en {matiere} est de {notes[index]}/20 ")

        elif choix2==((len(matieres))+1): 
            totalNotes=sum(notes)
            moyenneGenerale=totalNotes/(len(notes))
            print("-")
            print(f"Votre moyenne générale non pondérée est de {moyenneGenerale}/20.")

        elif choix2==((len(matieres))+2): 
            break

        else: 
            print("-")
            print("Je n'ai pas compris votre choix. Pouvez-vous rééssayer? Je rappelle: ")


    except ValueError: 
        print("-")
        print("Je n'ai pas compris votre choix2. Pouvez-vous rééssayer? Je rappelle: ")