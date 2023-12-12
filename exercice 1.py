def replace_star(mot):
    count = len(mot)
    mot = ""
    while count > 0:
        mot += "*"
        count -= 1
    return mot

mot = input("Quel est votre mot :")
print(replace_star(mot))