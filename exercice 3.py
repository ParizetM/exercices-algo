def ftn_somme(nb1,nb2):
    return nb1 + nb2
def isnumeric(nb):
    try :
        nb = float(nb)
        return True
    except ValueError :
        print("format de valeur incorrect")
        return False

sortie = False
t_nb =[]
somme_total = 0
while sortie != True :
    nombre = input("donnez un nombre :")
    if isnumeric(nombre) == False :
        sortie = False
    else :
        nombre = float(nombre)
        if nombre == 0 :
            sortie = False
            print("le nombre ne peux pas etre egal a 0")
        else:
            t_nb.append(nombre)
            somme_total = ftn_somme(somme_total,nombre)

            if somme_total >= 100:
                sortie = True
sortie = False
print(" la valeur est superieur a 100",t_nb)
while sortie != True :
    index_1 = input("donnez un premier chiffre d'index")
    if isnumeric(index_1) == True:
        sortie = True
        index_1 = int(index_1)
sortie = False
while sortie != True :
    index_2 = input("donnez un second chiffre d'index")
    if isnumeric(index_1) == True:
        sortie = True
        index_2 = int(index_2)

print("la somme des nombres choisi est :",ftn_somme(t_nb[index_1],t_nb[index_2]))
