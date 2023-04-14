from random import randint

d = randint(1,6)

print("Vous avez fait",d)

if d == 1 :
    print("┌───┐")
    print("| • |")
    print("└───┘")

elif d == 2 :
    print("┌───┐")
    print("|• •|")
    print("└───┘")

elif d == 3 :
    print("┌•────┐")
    print("|  •  |")
    print("└────•┘")

elif d == 4 :
    print("┌•───•┐")
    print("|     |")
    print("└•───•┘")

elif d == 5 :
    print("┌•───•┐")
    print("|  •  |")
    print("└•───•┘")

elif d == 6 :
    print("┌•───•┐")
    print("|•   •|")
    print("└•───•┘")