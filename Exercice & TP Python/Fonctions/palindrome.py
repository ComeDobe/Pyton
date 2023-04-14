"""
Palindrome


Écrivez une fonction qui teste une chaîne de caractères et retourne un booléen. Sa valeur sera VRAI si la chaîne
est un palindrome. Un palindrome est un texte qui se lit de la même façon à partir de la droite et de la gauche.
Il ne faut tenir compte que des lettres et ignorer les espaces et la ponctuation. Pour que les palindromes soient
plus faciles à tester, on suppose qu’ils sont saisis en majuscules uniquement.
Exemples :

• ELLE,

• LAVAL,

• ESOPE RESTE ICI ET SE REPOSE (à condition d’ignorer les espaces).
• TU L’AS TROP ECRASE, CESAR, CE PORT SALUT.

• ERIC, NOTRE VALET, ALLA TE LAVER TON CIRE.

• UN ROC LAMINA L’ANIMAL CORNU

• ELU PAR CETTE CRAPULE

• ENGAGE LE JEU QUE JE LE GAGNE

• OH, CELA TE PERD, REPETA L’ECHO

• L’AME SURE RUSE MAL

• LA MARIEE IRA MAL

• LEON A TROP PAR RAPPORT A NOEL

• ET LA MARINE VA VENIR A MALTE

• LA MALADE PEDALA MAL


"""


from lib2to3.pygram import python_grammar_no_print_statement


def palindrome(phrase_bis):
    variable = True
    i = 0
    while variable == True and i < len(phrase_bis) :
        if phrase_bis[i] == phrase_bis[len(phrase_bis)-i-1] :
                variable = True
        else :
            variable = False
        i = i + 1
    return  variable
phrase_bis = input(" saisir votre phrase : ")
reponse=palindrome(phrase_bis)
# print(phrase_bis,reponse)
print(palindrome(phrase_bis))










