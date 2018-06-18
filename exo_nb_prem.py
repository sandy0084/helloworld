# def nbPrem(n):
#     if n % 2 != 0 and n % 3 != 0 and n % 4 != 0 and n % 5 != 0 and n % 6 != 0 and n % 7 != 0 and n % 8 != 0 and n % 9 != 0 and n % 10 != 0:
#         return True
#     else:
#         return False
#
# print(nbPrem(5))

def nbPrem(n):
    for i in range(2,n-1):
        if n % i == 0:
            # print(str(n) + " divisible par " + str(i))
            return False
    return True

# v = nbPrem(5)
# v1 = nbPrem(10)
#
# print(v)
# print(v1)

##################
# def listNb(n):
#     list = []
#     for i in range(2,99):
#         nbPrem(n)
#         list.append(n)
#         print(list)
#         return


def listNb():
    for n in range(2,99):
        if nbPrem(n) == True:
            print("Nombre premier " + str(n))

listNb()