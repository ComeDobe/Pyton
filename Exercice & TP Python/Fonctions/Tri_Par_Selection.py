from random import*

def list_alea(n):
    
    s=[0]*n
    for i in range(n):
        s[i]=randrange(1,10000)
    return s

def tri_selection(T):
    for i in range(0, len(T)-1):
        min= T[i]
        indice =i
        for j in range(i+1, len(T)):
            if T[j]<min:
                min=T[j]  
                indice = j
        tmp = T[i]
        T[i] = T[indice]
        T[indice] = tmp
        
    # programme principal
    
tab1 = list_alea(20)
print(" le tableau non trié est ", tab1)

tri_selection(tab1)
print(" le tableau trié est ", tab1)