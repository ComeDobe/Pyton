
"""
Calculez la moyenne des notes d’un élève après avoir saisi les notes de français, de math, de
géométrie et d’informatique.

"""


subjects=['francais', 'maths', 'geometrie', 'info']

notes = []
total = 0
#for (index,subject) in enumerate(subject):   # indexer une valeur
    #print(f"{index}: {subject}")
    
#for i in range(0, len(subject)):  # compteur
    
    #print(subject[i])
    
for subject in subjects:  # afficher une valeur

    note=int(input(f"veuillez saisir la {subjects} : "))
    total += note
    
moyenne = total /len(subjects)
    
print(f" la moyenne est de {moyenne}/20 ")

    
    
