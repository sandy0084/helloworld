from random import randint
import random

nbSimulation = 10

def montyHall():
    for i in range(1, nbSimulation):
        pactole = randint(1,3)
        question1 = raw_input("Choisissez une porte entre 1 et 3 : ")
        question2 = raw_input("Voulez-vous conserver votre choix ? o/n ")
        if question2 == "o":
            if pactole == question1:
                print("Vous avez gagne !!!")
            else:
                print("Vous avez perdu !!!")
        if question2 == "n":
            question3 = raw_input("Choisissez une autre porte entre 1 et 3 : ")
            if pactole == question3:
                print("Vous avez gagne !!!")
            else:
                print("Vous avez perdu !!!")


montyHall()
