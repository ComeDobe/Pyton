
"""
calcul moyenne avec la liste

li=[ 10, 12, 15, 20,23, 14, 20]

s=0

for i in range(0,len(li)):
    
    s=s+li[i]
    
    print(s)
    print(s/len(li))
    
    """
    
    
    #calcul moyenne avec le coef ponderé
    

from re import L


li=[ 10, 12, 15, 20,23, 14, 20]
ci=[5, 4, 2, 3 ,6, 8,7]

s=0

for i in range( 0,len(li)):
    
    s+=li[i]*ci[i]
    
    
    print(s/ci[i])
   
 