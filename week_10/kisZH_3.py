class Teglalap :
    def __init__(self, width, height) :
        self.width = width
        self.height = height
    
    def __str__(self) :
        return "({} x {})".format(self.width, self.height)
#

def beolvas() :
    print("Add meg a teglalap szelesseget!")
    width = float(input())
    print("Add meg a teglalap magassagat!")
    height = float(input())
    return Teglalap(width, height)
#

def terulet(t) :
    return t.width * t.height
#

def main() :
    t1 = beolvas()
    t2 = beolvas()
    
    print("Az elso teglalap:", t1)
    print("A masodik teglalap:", t2)
    
    if terulet(t1) > terulet(t2) :
        print("Az elso a nagyobb teruletu.")
    else :
        print("A masodik a nagyobb teruletu.")
#

main()




