

distance=int(input("distance residence lieu de travail "))
jour=int(input( " jour de remplacement"))

Tauxind15 = 12.5
Tauxind30 = 23.5
Tauxind45 =30
Repas = 15
Bonus = 7

if distance<15:
    indemnitéjour = Tauxind15 + Repas*2
    indemnitétotale = indemnitéjour*jour
    print(" le taux d'indemnité est", indemnitéjour, "et l'indemnité totale est ", indemnitétotale)

elif distance < 30:
    indemnitéjour = Tauxind15 + Repas*2
    indemnitétotale = indemnitéjour*jour
    print(" le taux d'indemnité est", indemnitéjour, "et l'indemnité totale est", indemnitétotale)

elif distance < 45:
    indemnitéjour = Tauxind15 + Repas*2
    indemnitétotale = indemnitéjour*jour
    print(" le taux d'indemnité est", indemnitéjour, "et l'indemnité totale est", indemnitétotale)

elif distance < 65:
    indemnitéjour = Tauxind15 + Bonus + Repas*2
    indemnitétotale = indemnitéjour*jour
    print(" le taux d'indemnité est", indemnitéjour, "et l'indemnité totale est", indemnitétotale)

elif distance < 85:
    indemnitéjour = Tauxind15 + Bonus*2 + Repas*2
    indemnitétotale = indemnitéjour*jour
    print(" le taux d'indemnité est", indemnitéjour, "et l'indemnité totale est", indemnitétotale)

elif distance < 105:
    indemnitéjour = Tauxind15 + Bonus*3 + Repas*2
    indemnitétotale = indemnitéjour*jour
    print(" le taux d'indemnité est", indemnitéjour, "et l'indemnité totale est", indemnitétotale)