

def anag1(str1, str2):
    return sorted(str1)==sorted(str2)

print(anag1("chien","chine"))
print("ces deux mots sont des anagrammes")


def anag2(str1,str2):
    liste1=list(str1)
    liste2=list(str2)
    print("liste1", liste1)
    liste1.sort()
    print("liste2", liste2)
    liste2.sort()
    
    return (liste1==liste2)
print(anag2("chien","chine"))


# on utilise counter pour compter chaque nombre de lettre dans le mot.

from collections import Counter

def anag3(str1,str2):
    c1=Counter(str1)
    print("c1", c1)
    c2=Counter(str2)
    print("c2", c2)
    return c1==c2

print("compte le nombre de lettre ")    

# compte de lettre et verification d'anagramme: si c'est le cas on a un retour true, dans le cas contraire la fonction retourne false.
 
print(anag3("marion","marioon"))  


    

    

    