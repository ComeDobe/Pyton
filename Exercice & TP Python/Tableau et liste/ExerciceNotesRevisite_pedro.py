"""
1 - Afficher les notes
2 - Afficher la note de Maths, Fr, Geo, Info, etc
3 - Calculer la moyenne
"""

matieres=[]
notes=[]

#Table de matières+notes fictives pour tests du programme. Enlever les """ pour utiliser.

# matieres=["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh"] #notes deja créées pour test du programme
# notes=[11, 12, 13, 14, 15, 16, 17, 18]


print("Pour commencer, créez des matières et insérez-y votre moyenne. ")


while True: #Menu1: Créer/Supprimer des matières et des notes
     print("-")
     print("Pour créer de nouvelles matières, entrez new.")
     print("Pour supprimer des matières, entrez <<Supprimer>>.")
     print("Pour passer à la consultation des notes, entrez cons.")
     print("Pour quitter le programme complètement, entrez quit")
     choix1=input("")

     if choix1.lower()=="": #sous-menu création de nouvelles matieres + insertion de la note
        while True:
            print("-")
            print("Pour arrêter de créer de nouvelles matières et revenir au menu précédent, entrez <<Retour>>.")
            nouvelleMatiere=input("Quel est le nom de la matière à créer? ")
            if nouvelleMatiere.lower()=="retour":
                break
            else:  
                matieres.append(nouvelleMatiere)
            
            try: #pour eviter une saisie non numerique
                nouvelleNote=int(input(f"Combien avez-vous obtenu en {nouvelleMatiere}? "))
                notes.append(nouvelleNote)
            except ValueError:
                print("Note invalide. Matière non créée.")
                matieres.pop(-1)

     elif choix1.lower()=="": #sous-menu suppression de matières
        print("---Suppression---")
        while True:    
            
            for (index,matiere) in enumerate (matieres):
                print(f"Pour supprimer votre moyenne en {matiere}, entrez {index}.")
            print("Pour sortir du menu suppression, entrez <<Retour>>")
            suppression=input("")

            if suppression.lower()=="":
                break                
            elif int(suppression)>=0 and int(suppression)<len(matieres):
                matieres.pop(int(suppression))
                notes.pop(int(suppression))
            else: 
                print("-")
                print("Je n'ai pas compris. Voulez-vous dire <<Retour>>? ")

            

     elif choix1.lower()=="consulter": #Quitter la boucle du premier menu et passer à la suite
        break
    
     elif choix1.lower()=="quitter":
        break

     else:
        print("Je n'ai pas compris votre choix. Rééssayez:")



#Menu+Actions
while True:
    if choix1.lower()=="quitter": #bypass du menu consultations au cas ou l'utilisateur veut quitter dès le menu précédent
        break

    try: #pour checker que l'utilisateur peut faire des erreurs de saisie sans interrompre le programme
        print("-")
        for (index, matiere) in enumerate (matieres): #afficher chaque matiere avec son index comme option menu
            print(f"Pour afficher la note de {matiere}, entrez {index}")
            

        print(f"Pour afficher toutes les notes ensemble, entrez {len(matieres)}") #autres options sont en longueur de la liste de matieres +1 +2 +3
        print(f"Pour afficher la moyenne générale, entrez {len(matieres)+1}")
        print(f"Pour arrêter le programme, entrez {len(matieres)+2}")

        choix2=int(input()) #choix2 utilisateur pour le menu

        if choix2>=0 and choix2<len(matieres): #voir notes individuelles
            print("-")
            print(f"Votre note en {matieres[choix2]} est de {notes[choix2]}/20.")

        elif choix2==(len(matieres)): #loop pour ressortir toutes les notes en 1 fois
            print("-")
            for (index, matiere) in enumerate(matieres):
                print(f"Votre moyenne en {matiere} est de {notes[index]}/20 ")

        elif choix2==((len(matieres))+1): #calcul moyenne simple
            totalNotes=sum(notes)
            moyenneGenerale=totalNotes/(len(notes))
            print("-")
            print(f"Votre moyenne générale non pondérée est de {moyenneGenerale}/20.")

        elif choix2==((len(matieres))+2): #arrêt du porgramme
            break

        else: #erreur de choix dans le menu
            print("-")
            print("Je n'ai pas compris votre choix. Pouvez-vous rééssayer? Je rappelle: ")


    except ValueError: #toute autre erreur de choix autre que mauvais numero tombe ici
        print("-")
        print("Je n'ai pas compris votre choix2. Pouvez-vous rééssayer? Je rappelle: ")