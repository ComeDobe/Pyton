
"""

Exercice 2 :
Demandez à saisir une date de la forme AAAA/MM/JJ (par exemple 2011/10/17) et afficher « Le
17 octobre 2011 est un lundi. » Pour connaitre le nom du jour, on part de la date avec :
• A = année complète (dans l’exemple 2011),
• M = numéro du mois (dans l’exemple 10),
• J = numéro du jour (dans l’exemple 17).
Si MM vaut 1 ou 2, il faut :
• retrancher 1 à A,
• ajouter 12 à M.
Avec ces valeurs, on calcule un nombre N
• N = J + ENT((13 * M + 3) / 5) + ENT(5 * A / 4)— ENT(A / 100) + ENT(A / 400)
• N = MOD(N ; 7)
N donne le nom du jour avec : 0 pour lundi, 1 pour mardi, ..., 6 pour dimanche


"""


date = input("Veuillez saisir une date au format AAAA/MM/JJ : ")

A = ""
M = ""
J = ""

for (i,c) in enumerate(date):
    if i >= 0 and i <= 3:

        A += c  #A = A + c

    elif i > 4 and i < 7:
        M += c
    elif i >= 8:
        J += c


A = int(A)
M = int(M)
J = int(J)

if M == 1 or M == 2:
    A = A - 1
    M = M + 12

N = J + int((13 * M + 3) / 5) + int(5 * A / 4) - int(A / 100) + int(A / 400)
N = N % 7

if N == 0:
    jour = "Lundi"
elif N == 1:
    jour = "Mardi"
elif N == 2:
    jour = "Mercredi"
elif N == 3:
    jour = "Jeudi"
elif N == 4:
    jour = "Vendredi"
elif N == 5:
    jour = "Samedi"
elif N == 6:
    jour = "Dimanche"

print(f"Le {J}/{M}/{A} est un {jour}")