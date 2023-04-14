
"""

Table V2

Saisissez un nombre entre 1 et 20, c’est le rang d’une table. Proposez ensuite un menu :
— table d’addition, saisir 1,
— table de multiplication, saisir 2,
— table des carrées, saisir 3,
— table des factorielles, saisir 4,
— pour sortir, saisir 5.
Demandez le choix de l’utilisateur et faites le traitement voulu.


"""



# table de multiplication
while True:

 n=int(input("saisissez une table:"))
 print("la table de multiplication de n est  egale à : ")
 for i in range ( 1, 10 ):

  print(i, "x", n , "=", i*n)

  
     # table d'addition
 while True:


  n=int(input("saisissez une table:"))
  print("la table d'addition de n est  egale à : ")
  for i in range ( 1,10 ):

     print(i, "+", n , "=", i+n)



  break

# table de carrée
 
 print("la table d'addition de n est  egale à : ")
 for i in range ( 1,10):

     print(i, "=", i*i)
      

 break
# table de factorielle

s = ""
x = 1
for i in range(1,6):
    x = x* i
    s = ""
    for j in range(1,i+1):
        s += str(j) +'x '
        print (s[-1:],"=",x)

     
       

