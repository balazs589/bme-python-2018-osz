
# =============================================================================
# import:

import math

# =============================================================================
# osztalyok, fuggvenyek:

# -----------------------------------------------------------------------------

class Pont:
    def __init__(self, p1=None, p2=None) :
        if type(p1) is float and type(p2) is float :
            x = p1
            y = p2
        elif type(p1) is str and p2 is None :
            koordinatak = p1.split()
            x = float(koordinatak[0])
            y = float(koordinatak[1])
        elif p1 is None and p2 is None :
            x = 0.0
            y = 0.0
        else :
            raise TypeError("Nem megfelelo konstruktorhivas!")
        self.x = x
        self.y = y
    
    def __eq__(self, jobb) :
        return self.x == jobb.x and self.y == jobb.y
    
    def __ne__(self, jobb) :
        return not __eq__(self, jobb)
    
    def __sub__(self, jobb) :
        return Pont(self.x - jobb.x, self.y - jobb.y)
    
    def __abs__(self) :
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
#

def tav(p1, p2) :
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
#

def egyenlo(p1, p2) :
    return p1.x == p2.x and p1.y == p2.y    # float: valodi ertekeknel nem sok ertelme van
#

def beolvas() :
    x = float(input("x : "))
    y = float(input("y : "))
    return Pont(x, y)
    
#



# -----------------------------------------------------------------------------

def main():
    origo = Pont(0.0, 0.0)
    p1 = Pont(3.0, 4.0)
    print(tav(p1, origo))
    
    p2 = beolvas()
    
    print(egyenlo(p1, p2))
    
    
    # -------------------------------------------------------------------------
    # 1. megoldas
    print("-" * 79)
    
    pontok1 = []
    print("\nAdd meg a torespont x es y koordinatait!")
    pontok1.append(beolvas())
    osszes_husszusag = 0.0
    
    while True :
        print("\nAdd meg a torespont x es y koordinatait!")
        pontok1.append(beolvas())
        tavolsag = tav(pontok1[-1], pontok1[-2])
        osszes_husszusag += tavolsag
        print("tavolsag = {}, osszes_husszusag = {}".format(tavolsag, osszes_husszusag))
        if egyenlo(pontok1[0], pontok1[-1]) :
            break
    
    
    
    
    # -------------------------------------------------------------------------
    # 2. megoldas
    print("-" * 79)
    print("operator overloadinggal:")
    print()
    
    pontok2 = []
    print("\nAdd meg a torespont x es y koordinatait, szokozzel elvalasztva egy sorban!")
    pontok2.append(Pont(input()))
    osszes_husszusag2 = 0.0
    
    while True :
        print("\nAdd meg a torespont x es y koordinatait!")
        pontok2.append(Pont(input()))
        tavolsag2 = abs(pontok2[-1] - pontok2[-2])
        osszes_husszusag2 += tavolsag2
        print("tavolsag2 = {}, osszes_husszusag2 = {}".format(tavolsag2, osszes_husszusag2))
        if pontok2[0] == pontok2[-1] :
            break
    
    
    
    
#


# =============================================================================
# futtatas:


main()









