# T = [1,2,3,4,5]
#
# T2 = [6,7,8,9,10]
#
# def inTableau(i):
#     for i in T:
#         if i in T:
#             return i
#
#
#
# inTableau(1)


def inArray(table, val):
    isInArray = False
    for i in table:
        if i == val:
            isInArray = True
            print('La variable',i, 'est dans le tableau')

    if isInArray == False:
        print('La variable', val, "n'est pas dans le tableau")

def inArray2(table, val):
    for i in table:
        if i == val:
            print('La variable',i, 'est dans le tableau')
            return

    print('La variable', val, "n'est pas dans le tableau")


inArray([1,2,3,4,5],6)
inArray([1,2,3,4,5],2)

inArray2([1,2,3,4,5],6)
inArray2([1,2,3,4,5],2)