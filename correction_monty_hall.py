from random import randint
import random

def simulation(nbSimulation, changeChoix):

    nbVictoires = 0

    for i in range(1, nbSimulation):

        portes = [1, 2, 3]

        pactole = random.choice(portes)
        choix1 = random.choice(portes)

        porteRestanteVide = [1, 2, 3]
        porteRestanteVide.remove(pactole)

        if pactole != choix1:
            porteRestanteVide.remove(choix1)

        porteSupprimee = random.choice(porteRestanteVide)

        if not changeChoix:
            choix2 = choix1
        else:
            p = [1, 2, 3]
            p.remove(choix1)
            p.remove(porteSupprimee)
            choix2 = p[0]

        if choix2 == pactole:
            nbVictoires = nbVictoires + 1

        # print("-----------------------")
        # print("Pactole = " + str(pactole))
        # print("Choix 1 = " + str(choix1))
        # print(porteRestanteVide)
        # print("Porte supprimee = " + str(porteSupprimee))

    successPercent = float(nbVictoires) / float(nbSimulation) * 100

    print("Success percent = " + str(successPercent) + "%")

simulation(1000, False)
simulation(1000, True)