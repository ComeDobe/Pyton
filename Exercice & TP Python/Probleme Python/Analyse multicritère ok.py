
"""

Analyse multicritères

Cet algorithme est une approche de l’intelligence artificielle. Il doit
poser une suite de questions pour découvrir l’animal que vous avez
choisi. La recherche se fait par une recherche en arborescence, par
exemple :
— L’animal est-il mammifère ou ovipare ?
— s’il est ovipare, est-il à plume ou à écaille ?
— s’il est à plume, c’est un oiseau.
— s’il est à écaille, vit-il dans l’eau ?
— s’il vit sur terre, c’est un reptile.
— si c’est un mammifère, vit-il dans l’eau ou sur terre ?
— s’il vit dans l’eau, c’est un cétacé.
— s’il vit sur terre, fait-il « miaou » ou « wouah-wouah » ?
— s’il fait « miaou », c’est un chat.

"""

animal = input("Choisir si l'animal est un mammifère ou un ovipare : ")
if animal == "mammifère" :
    mammifère = input("Vit-il dans l'eau ou sur terre ? ")
    if mammifère == "eau" :
        print("C'est un cétacé.")
    elif mammifère == "terre" :
        mammifère = input("Fait-il miaou ou wouah-wouah ? ")
        if mammifère == "miaou" :
            print("C'est un chat.")
        elif mammifère == "wouah-wouah" :
            print("C'est un chien.")
if animal == "ovipare" :
    ovipare = input("Est-il à plume ou a écaille ? ")
    if ovipare == "plume" :
        print("C'est un oiseau.")
    elif ovipare == "écaille" :
        ovipare = input("Vit-il dans l'eau ou sur terre ? ")
        if ovipare == "eau" :
            print("C'est un poisson.")
        elif ovipare == "terre" :
            print("C'est un reptile.")