def compter_cara(mot) :
    return len(mot)
sortie = False
i = 0
tableau_num = []
while sortie != True :
    mot = input("Donnez un mot :")
    tableau_num.append(compter_cara(mot))
    if mot.lower() == "stop":
        sortie = True
        print(tableau_num)
    else :
        sortie = False

