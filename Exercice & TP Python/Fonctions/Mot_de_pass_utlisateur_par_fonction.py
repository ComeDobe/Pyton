

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

def pass_word():
    
    lives=3
    user="bonjour"
    secret="minou"


    user_password=input(f"saisir un mot de passe, vous avez {lives} essai: ")

    for i in range(0, lives):
        
        if user_password!=user:
            lives=lives-1
            print(f" attention il vous reste {lives} essai")
            user_password=input(f"saisir un mot de passe vous avez {lives} essai: ")
        if lives==0:
            print(" je vous donne une derniere chance ")
            answer=input(" à quoi reconnait-on un chat ?, un indice le son :")
        
            if answer==secret or answer=="minou":
                print(" bienvenu dans la session")
            elif answer!="minou":
                print(" compte bloqué ") 
                
        if  user_password==user or user_password==" bonjour":
            print(" authenfication reussi ")      
pass_word()
            
            
            
        
