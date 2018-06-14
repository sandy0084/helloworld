import random
import math

################ Fonctions utiles #########
# x = random.random()
# print(x)
# y = random.random()
#
# dist = math.sqrt(x * x + y * y)
#
# print(dist)
#
# for i in range(1,10) :
#     print(i)

################## Exo Moi ############
# x = random.random()
# print(x)
# y = random.random()
# print(y)
#
# for i in range(x,y) :
#     print(i)

################## Correction ############
iteration = 1000
total = 0

for i in range(1, iteration) :
    x = random.random()
    y = random.random()

    dist = math.sqrt(x * x + y * y)

    if dist <= 1:
        total = total + 1

# aire cercle = pi x r x r (ici r = 1)
# aire quart cercle = pi / 4
pi = float(total) / float(iteration) * 4

print(total)
print(iteration)
print(total / iteration)
print(total / iteration * 4)
print(pi)