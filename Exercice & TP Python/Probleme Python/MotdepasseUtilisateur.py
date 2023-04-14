"""

Mot de passe ? (Caput Draconis) :
Ecrire un algorithme qui permet de vérifier le mot de passe saisi au clavier. L’utilisateur a
droit à 3 chances pour que la machine lui affiche le succès de l’authentification sinon un 
message de compte bloqué sera affiché. 
Dans le cas où il veut encore retenter l’accès au compte une nouvelle chance lui est proposée 
sous forme de question secrète à laquelle il devra répondre. Si la réponse est incorrecte l’accès 
lui est définitivement refusé pour l’exécution en cours. 
Note : le mot de passe correct est ‘Bonjour’ et la réponse correcte à la question secrète est 
‘Minou’

"""

reponse="minou"
motdepasse="bonjour"
motdepasseUtilisateur=""
essais=3

motdepasseUtilisateur = input("Entrez votre mot de passe : ")

while essais > 0:
 if motdepasseUtilisateur != motdepasse:
    print(" accés refusé")
    
    break
 elif motdepasseUtilisateur== motdepasse:

    print("Accès autorisé")
    quit()
    
print(" il vous reste deux chances")
motdepasseUtilisateur = input("Entrez votre mot de passe : ")

print(" c'est votre derniere chance")
motdepasseUtilisateur = input("Entrez votre mot de passe pour la derniere fois: ")

reponse = input("Donnez le synonyme d'une chatte?")

if reponse == "minou":
    print("Accès autorisé")
else:
    print("Accès refusé")
