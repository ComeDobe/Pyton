
import datetime
from distutils.log import error

time=datetime.datetime.now()

print (time)


jours=""

print(" year", time.year)


def jours_année(numero):
    if jours==1:
     return "lundi"
    elif jours==2:
     return "mardi"
    elif jours==3:
     return "mercredi"
    elif jours==4:
         return "jeudi"
    elif jours==5:
     return "vendredi"
    elif jours==6:
     return "samedi"
    elif jours==7:
     return "dimanche"
 
def mois_année(numero):
    if numero==1:
        return "janvier"
    elif numero==2:
        return " fevrier"
    elif numero==3:
        return "mars"
    elif numero==4:
        return "avril"
    elif numero==5:
        return "mai"
    elif numero==6:
        return " juin"
    elif numero==7:
        return "juillet"
    elif numero==8:
        return " aout"
    elif numero==9:
        return "sept"
    elif numero==10:
        return " oct"
    elif numero==11:
        return "nov"
    elif numero==12:
        return " dec"
    return error

mois=mois_année(10)
jpurs=jours_année(5)

print(mois)
print( jours)



