

from gettext import find


ran3 = ["Yasmina","Carolina","David","Nathan","Gerald","Florian","Nicolas","Thomas","Hervé","Maxence","Christian","Florian","Alexandre","Nathan","Pedro","Julien"]


# element = input("cherchez un prenom:")

# if element in ran3: 
#     print(f"{element} est dans la liste de la ran3" )
# else:
#     print(f" {element} n'est pas dans la liste de la ran3 " )

firstnametofind=input("cherchez un prenom")
find=False
for index, firstname in enumerate(ran3):
     if firstname.upper()==firstnametofind.upper():                      #.upper() convertit en majuscule
        print(f" trouvé à l'index {index} ")
        find=True
        break
     if not find:
         print(f"il n'a pas de {firstnametofind} dans la liste...")
         
ran3.sort()       # .sort() est utilisé pour le tri
print(ran3)
        
    


