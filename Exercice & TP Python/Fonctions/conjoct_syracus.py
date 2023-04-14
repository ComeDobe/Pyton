"""

Syracuse

La conjecture de Syracuse est une suite numérique, énoncée dans les années 1930, dont le fonctionnement n’a
jamais été démontré.

Il a été vérifié pour un certain nombre de valeurs de départ, mais aucune démonstration
n’a jamais expliqué son fonctionnement.
Le principe de la suite est le suivant :

• prenez un entier positif,

• s’il est impair, multipliez-le par 3 et ajoutez 1,

• s’il est pair, divisez-le par 2.

Prenons le nombre 7 comme point de départ.

La suite obtenue est : 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5,
16, 8, 4, 2, 1, 4, 2, 1…

Arrivés ici, les résultats se reproduisent cycliquement parce que la valeur 1 fait boucler
l’algorithme.

Écrivons l’algorithme qui essaye cette conjecture pour un nombre saisi au clavier.


"""

def conjocture_syracus():
    
    v=int(input(" saisir une valeur "))
    liste=[]
    compteur=0
    if v!=0:
        while v!=1:
            if v%2==0:            
                v=v/2                  # si v est paire on le divise par 2
                liste.append(v)
                compteur=compteur+1      # on incremente le compteur 
            else:
                v=3*v+1             # si v est impaire on le multiplie par 3 et on ajoute 1
                liste.append(v)
                compteur=compteur+1
            print("la valeur 1 est atteinte en ", compteur, " coups" )
            print("")
            print(liste)   # on affiche les valeurs de la suite 
    return liste
            
conjocture_syracus()
   