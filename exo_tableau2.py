def tableauIndice(array,var):
    k = 0
    indice = []
    for i in array:
        if i == var:
            indice.append(k)
        k = k + 1
        print(indice)



def tableauIndice2(t, n):
    t2 = []
    for i in range(0, len(t)):
        if n == t[i]:
            t2.append(i)
    print(t2)


tableauIndice([3,5,0,4,4,7],5)
tableauIndice([3,5,0,4,4,7],4)
tableauIndice([3,5,0,4,4,7],8)

tableauIndice2([3,5,0,4,4,7],5)
tableauIndice2([3,5,0,4,4,7],4)
tableauIndice2([3,5,0,4,4,7],8)