def cleanStr(term: str) -> str:
    """
    Permet de retourner une chaîne de caractères sans accents :D
    """
    a = ["a","à","â"]
    e = ["e","é","è","ê"]
    i = ["i","î","ï"]
    o = ["o","ô","ö"]
    u = ["u","û","ù"]
    c = ["c","ç"]
    s = ["","'","/"," ","\"",",",".","’"]
    letters = [a,e,i,o,u,c,s]
    res = ""
    term = term.lower()
    for char in term:
        for tab in letters:
            if char in tab[1:]:
                char = tab[0]
        res += char
    return res

def inverseStr(term: str) -> str:
    """
    Permet d'inverser une chaîne de caractères
    """
    res = ""
    for char in term:
        res = char + res
    return res


def isPalindrome(term: str) -> bool:
    """
    Permet de vérifier si un chaîne de caractères est un palindrome.
    """
    # termCleaned = cleanStr(term)
    # print(termCleaned)
    # termInversed = inverseStr(termCleaned)
    # print(termInversed)
    # if termCleaned == termInversed:
    #     return True
    # else:
    #     return False
    # Pour les petits bébés dév :D

    return cleanStr(term) == inverseStr(cleanStr(term))



# if isPalindrome(input("Est-ce un palindrome ? : ")):
#     print("C'est un palindrome !")
# else:
#     print("Nope.")
 
print("C'est un palindrome !") if isPalindrome(input("Est-ce un palindrome ? : ")) else print("Nope.")

# Exemple affectation en ternaire
# res = "Oui" if isPalindrome("kayak") else "Nope"
