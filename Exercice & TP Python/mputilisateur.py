            
            
            


mdpJoueur=input("Mot de passe ?\n")
lives=3
while lives>0:           
            lives=3
            motdepasse="Bonjour"
            mdpJoueur=""
            answer=""  
            if mdpJoueur!=motdepasse:
                
                lives=lives-1

            if lives==2:
            
                print("FAUX. Vous pouvez réessayer, il vous reste deux essais.")
            elif lives==1:
                print("Réessayez, mais attention, c'est votre dernière chance.")
            else:
                print("Entrez, je vous prie.")

                quit()
            
            print("Quel est le nom de la fleur mâle du noyer ?")

            if answer=="Minou" or answer=="minou" or answer=="Le minou" or answer=="le minou":
                print("Hmpf... Vous pouvez entrer.")
            
            else:
                print("Eh bien tant pis. Au revoir.")
                
            quit()