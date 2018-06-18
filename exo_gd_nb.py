def grandNb():
    list = []
    for i in range(1,10):
        nb = raw_input("Entrez un nombre : ")
        list.append(i)
        print(list)

grandNb()


def comparateur():
    max = 0
    for i in range(0,10):
        chiffre = raw_input("Entrez un chiffre : ")
        if(int(chiffre) > int(max)):
            max = int(chiffre)
    print("Le plus grand chiffre que vous avez entre est " + str(max))

comparateur()