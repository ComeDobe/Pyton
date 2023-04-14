date = input("Veuillez saisir une date au format AAAA/MM/JJ : ")

A = ""
M = ""
J = ""

for (i,c) in enumerate(date):
    if i >= 0 and i <= 3:
        #A = A + c
        A += c
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