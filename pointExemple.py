import math

class Point:

    #constructeur
    def __init__(self, x, y):
        #attribut
        self.x = x
        self.y = y

    #declarer une methode
    def distorigin(self):
        dist = math.sqrt(self.x * self.x + self.y * self.y)
        return dist

pt1 = Point(2,3)
pt2 = Point(7,2)

Point(pt1.distorigin())
Point(pt2.distorigin())