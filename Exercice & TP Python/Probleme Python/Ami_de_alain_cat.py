


# Alain et Catherine organisent une soirée pour des membres de leur club informatique.
# Ils décident que pour être invité il faut :

# - être ami d’Alain et de Catherine ;
# - ou ne pas être ami d’Alain, mais être ami de Catherine ;
# - ou ne pas être ami de Catherine, mais jouer au bridge.

# Pour un membre quelconque, on définit les variables booléennes suivantes par :
# a = 1 s’il est un ami d’Alain,
# b = 1 s’il joue au bridge,
# c = 1 s’il est un ami de Catherine.



a=int(input("tu es ami d'alain ? "))
b=int(input("tu joues au bridge? "))
c=int(input("tu es ami de catherine ? "))

print((a==1 and c==1) or (a==0 and c==1) or(b==1 and c==0))  # ou print(0 or 0)

