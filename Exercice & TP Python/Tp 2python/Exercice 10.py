

"""

Exercice 10 :

Le contrôle d’une centrale nucléaire se fait par l’examen de températures.
Si la différence entre la température ambiante et la température des bassins de refroidissement est
inférieure à 20 °C ou si elle dépasse 40 °C, affichez une alarme.

"""

while True :
    try :
        TempAmb = float(input("Saisir la température ambiante : "))
        TempBassin = float(input("Saisie la température des bassins de refroidissement : "))
        if TempAmb < 0 or TempBassin < 0 :
            print("Veuillez saisir des valeurs positives uniquement")

        elif TempAmb >= TempBassin :
            DiffTemp = TempAmb - TempBassin
            if DiffTemp < 20 or DiffTemp > 40 :
                print("Alerte")
                break
            else :
                print("Température normal.")
                break
        elif TempBassin > TempAmb :
            DiffTemp = TempBassin - TempAmb
            if DiffTemp < 20 or DiffTemp > 40 :
                print("Alerte") 
                break
            else :
                print("Température normal")
                break
    except ValueError :
        print("Entrez une valeur numérique")