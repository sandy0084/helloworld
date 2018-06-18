def fibonacci():
    n2 = 0
    n1 = 1
    for i in range(1,20):
        v = n1 + n2
        n2 = n1
        n1 = v
        print(v)

fibonacci()