def compter_cara(mot) :
    return len(mot)
sortie = False
while sortie != True :
    mot = input("Donnez un mot :")
    if mot.lower() == "stop":
        sortie = True
    else :
        sortie = False
        print(compter_cara(mot))
