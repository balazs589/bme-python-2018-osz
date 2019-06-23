

class Doge :
    def __init__(self, nev, papa_id=-1, mama_id=-1) :
        self.nev        = nev
        self.papa_id     = papa_id
        self.mama_id     = mama_id
    
#

def osszeset_kiir(doges) :
    for id, doge in doges.items() :
        print(doge.nev, id, doge.papa_id, doge.mama_id)
#

def keres(doges, id) :
    return doges[id] if id in doges else None
#

def torol(doges, id) :
    if id in doges :
        del doges[id]
        for doge in doges.values() :
            if doge.papa_id == id :
                doge.papa_id = -1
            if doge.mama_id == id :
                doge.mama_id = -1
    
#


def fajlba_kiir(doges, fajlnev) :
    with open(fajlnev, "wt", encoding="utf-8") as f :
        for id, doge in doges.items() :
            sor = str(id) + " " + doge.nev + " " + str(doge.papa_id) + " " + str(doge.mama_id) + "\n"
            f.write(sor)
    
#

def fajlbol_beolvas(fajlnev) :
    doges = {}
    with open(fajlnev, "rt", encoding="utf-8") as f :
        for sor in f :
            id, nev, papa_id, mama_id = sor.split()
            doges[id] = Doge(nev, papa_id, mama_id)
    return doges
#


def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    doges = {}
    names = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1, 20) :
        doges[i] = Doge(names[i-1])
        if i > 2 :
            doges[i].papa_id = 1
            doges[i].mama_id = 2
    
    for id, doge in doges.items() :
        print(id, doge.nev)
    
    print(                         elvalaszto_sor                         )
    osszeset_kiir(doges)
    
    
    print(                         elvalaszto_sor                         )
    
    torol(doges, 2)
    torol(doges, 10)
    torol(doges, 30)
    
    
    print(                         elvalaszto_sor                         )
    osszeset_kiir(doges)
    
    print(                         elvalaszto_sor                         )
    for id in range(1,25) :
        doge = keres(doges, id)
        if doge is not None :
            print("A kutya neve: {}".format(doge.nev))
        else :
            print("Nincs ilyen azonositoju kutya.")
    
    print(                         elvalaszto_sor                         )
    fajlba_kiir(doges, "doges.txt")
    
    
    print(                         elvalaszto_sor                         )
    print("Visszaolvasas fajlbol:")
    doges2 = fajlbol_beolvas("doges.txt")
    osszeset_kiir(doges2)
    
#


if __name__ == "__main__" :
    main()
#


