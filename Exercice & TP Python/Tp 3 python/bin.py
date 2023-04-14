
nombre = int(input("Veuillez saisir un entier : "))

while nombre < 0:
    nombre = int(input("Faux conditions! Veuillez saisir une autre fois : "))
    
if nombre == 0 or nombre == 1:

    print(nombre,"en binaire est:",nombre)
else:
    nombre_original = nombre

    string_binaire = ''
    while nombre > 1:
        n = nombre%2
        string_binaire += str(n)

        nombre = nombre // 2
    string_binaire += '1'

    string_binaire = string_binaire[::-1]

    print(nombre_original,"en binaire est:",string_binaire)