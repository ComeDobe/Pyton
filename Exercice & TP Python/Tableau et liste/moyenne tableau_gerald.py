# utilisation des tableaux pour le calcul de moyenne

# controle de la validité d"une note de type string donnée en paramètre
#   retourne la note de type float si elle est valide, sinon -1
def testNote(noteSaisie):   
    try:
        note = float(noteSaisie)
        if note<0 or note>20:
            raise TypeError
        else :
            return note
    except ValueError:
        return -1
    except TypeError:
        return -1

# gestion de l'affichage des menus/ sous-menu et controle de la validité des choix
#   retourne le menu choisi sous la forme de tableau [menu,sous-menu,sous-sous-menu]
def choixMenu():    
    nbMenu = 5
    nbSousMenu1 = len(tabMatiere)+2
    nbSousMenuGestion = 3
    tabMenu = []

    # affichage du menu principal    
    saisieOutNotValid = True
    while saisieOutNotValid:
        print("Menu")
        print("     1 - Saisir les notes")
        print("     2 - Afficher les notes")
        print("     3 - Afficher la moyenne")
        print("     4 - Gestion des matières")
        print("     5 - Quitter")
        # choix du menu
        try :
            menuSelected = int(input("votre choix ? : "))
            if menuSelected<1 or menuSelected>nbMenu:
                raise TypeError
            else :
                saisieOutNotValid = False
                tabMenu.append(menuSelected)
        except ValueError :
            print("un nombre entier est attendu")
        except TypeError :
            print("votre saisie ne correspond à aucun menu")

    # sous-menu ajout/modif note
    if tabMenu[0] == 1 :
        saisieInNotValid = True
        while saisieInNotValid:
            print("Sous-Menu : Saisir les notes")
            for i in range(0,len(tabMatiere)):
                print(f"         {i+1} - ajouter/modifier la note de {tabMatiere[i]}")
            print(f"         {i+2} - ajouter/modifier toutes les notes")
            print(f"         {i+3} - retour")
            try :
                sousMenuSelected = int(input("votre choix ? : "))
                if sousMenuSelected<1 or sousMenuSelected>nbSousMenu1:
                    raise TypeError
                else :
                    saisieInNotValid = False
                    tabMenu.append(sousMenuSelected)
            except ValueError :
                print("un chiffre est attendu")
            except TypeError :
                print("votre choix ne correspond à aucun sous-menu")
        return tabMenu

    # sous-menu afficher les notes
    if tabMenu[0] == 2 :
        saisieInNotValid = True
        while saisieInNotValid:
            print("Sous-menu : Afficher les notes")
            for i in range(0,len(tabMatiere)):
                print(f"         {i+1} - affichage de la note de {tabMatiere[i]}")
            print(f"         {i+2} - afficher toutes les notes")
            print(f"         {i+3} - retour")
            try :
                sousMenuSelected = int(input("votre choix ? : "))
                if sousMenuSelected<1 or sousMenuSelected>nbSousMenu1:
                    raise TypeError
                else :
                    saisieInNotValid = False
                    tabMenu.append(sousMenuSelected)
            except ValueError :
                print("un chiffre est attendu")
            except TypeError :
                print("votre choix ne correspond à aucun sous-menu")
        return tabMenu

    # sous-menu gestion des matières
    elif tabMenu[0] == 4 :
        saisieInNotValid = True
        while saisieInNotValid:
            print("Sous-menu : Gestion des matières")
            print("         1 - Ajouter une matière")
            print("         2 - Supprimer une matière")
            print("         3 - Retour")
            try :
                sousMenuSelected = int(input("votre choix ? : "))
                if sousMenuSelected<1 or sousMenuSelected>nbSousMenuGestion:
                    raise TypeError
                else :
                    saisieInNotValid = False
                    tabMenu.append(sousMenuSelected)
            except ValueError :
                print("un chiffre est attendu")
            except TypeError :
                print("votre choix ne correspond à aucun sous-menu")
        if tabMenu[1] == 1:
            return tabMenu
        elif sousMenuSelected == 2:
            # sous sous-menu supprimer matière
            saisieSuppNotValid = True
            while saisieSuppNotValid:
                print("Sous-menu : Gestion des matières")
                print("         1 - Ajouter une matière")
                print("         2 - Supprimer une matière")
                for i in range (0,len(tabMatiere)):
                    print(f"             {i+1} - {tabMatiere[i]}")
                print(f"             {i+2} - Retour")
                try :
                    sousMenu2Selected = int(input("votre choix ? : "))
                    if sousMenu2Selected<1 or sousMenu2Selected>len(tabMatiere)+1:
                        raise TypeError
                    else :
                        saisieSuppNotValid = False
                        tabMenu.append(sousMenu2Selected)
                except ValueError :
                    print("un chiffre est attendu")
                except TypeError :
                    print("votre choix ne correspond à aucun sous-menu")
            return tabMenu

    else :
        return tabMenu


# debut du programme principal

tabMatiere = ["Français","Maths","Géométrie","Informatique"]
tabNote = []

# initialisation du tableau de note
for i in range (0,len(tabMatiere)):
    tabNote.append(-1)

continuer = True
while continuer:
    menuChoisi = choixMenu()
    
    # Menu : saisie des notes
    if menuChoisi[0] == 1:
        index = menuChoisi[1] - 1
        if index < len(tabMatiere):
            tabNote[index] = -1
            while tabNote[index] < 0:
                tabNote[index] = testNote(input(f"saisir la note de {tabMatiere[index]} : "))
        elif index == len(tabMatiere):    
            for i in range(0,len(tabMatiere)):
                tabNote[i] = -1
                while tabNote[i] < 0:
                    tabNote[i] = testNote(input(f"saisir la note de {tabMatiere[i]} : "))
        else :
            pass

    # affichage des notes
    elif menuChoisi[0] == 2:
        index = menuChoisi[1] - 1
        if index < len(tabMatiere):
            if tabNote[index] < 0 :
                print(f"La note en {tabMatiere[index]} n'a pas été saisie")
            else :    
                print(f"La note en {tabMatiere[index]} est de {tabNote[index]}/20")
        elif index == len(tabMatiere):
            for i in range(0,len(tabMatiere)):
                if tabNote[i] < 0 :
                    print(f"La note en {tabMatiere[i]} n'a pas été saisie")
                else :
                    print(f"La note en {tabMatiere[i]} est de {tabNote[i]}/20")
        else :
            pass

    # calcul et affichage de la moyenne
    elif menuChoisi[0] == 3:
        manqueNote = False
        nbNote = 0
        moyenne = 0
        for i in range(0,len(tabNote)):
            if tabNote[i] < 0 :
                manqueNote = True
            else :
                moyenne += float(tabNote[i])
                nbNote += 1
        if nbNote == 0:
            print("Aucune note n'a été saisie")
        else :
            moyenne /= nbNote
            if manqueNote:
                print("Toutes les notes ne sont pas saisies, la moyenne provisoire est de {0:.2f}".format(moyenne),"/20")
            else :            
                print("La moyenne est de {0:.2f}".format(moyenne),"/20")

    # menu gestion des matières
    elif menuChoisi[0] == 4:
        if menuChoisi[1] == 1:
            # ajout d'une matière
            matiere = input("saisir la nouvelle matière : ")
            tabMatiere.append(matiere)
            tabNote.append(-1)
            print("La matière",matiere," a été ajoutée")

        elif menuChoisi[1] == 2:
            index = menuChoisi[2] - 1
            # supprimer la matiere sélectionnée
            if index < len(tabMatiere) :
                print(f"La matière {tabMatiere[index]} a été supprimée")
                if len(tabMatiere)-index > 1 : 
                    # décalage des matières situés après la matières supprimée vers la gauche
                    for i in range(index,(len(tabMatiere)-index)):
                        tabMatiere[i] = tabMatiere[i+1]
                        tabNote[i] = tabNote[i+1]
                # suppression du dernier élément
                tabMatiere.remove(tabMatiere[len(tabMatiere)-1])
                tabNote.remove(tabNote[len(tabNote)-1])
            else :
                pass

    # menu quitter
    elif menuChoisi[0] == 5:
        continuer = False
