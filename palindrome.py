# def palindrome(s):
#     size = len(s)
#     fin = size - 1
#     for c in range(0, size):
#         if(s[c] == s[fin]):
#             print("Non")
#             return False
#         fin = fin - 1
#     print("Oui")
#     return True
#
#
# palindrome("kayak")


def palindrome(text):
    l = len(text)
    indexFin = l - 1
    pal = False

    for i in range(0, l):
        if(text[i] == text[indexFin]):
            pal = True
        else:
            print("Le mot " + text + " n'est pas un palindrome")
            return
        indexFin = indexFin - 1

    if(pal == True):
        print("Le mot " + text + " est un palindrome")


palindrome("kayak")
palindrome("radar")
palindrome("anna")
palindrome("voisin")