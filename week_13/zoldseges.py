
def vasarlas(keszlet, arak) :
    
    vegosszeg = 0
    
    while True :
        rendeles = input()
        if rendeles == "" :
            break
        
        if rendeles not in keszlet or keszlet[rendeles] == 0 :
            print("Nincs raktaron.")
        else :
            print("OK")
            keszlet[rendeles] -= 1
            vegosszeg += arak[rendeles]
    
    print("Vegosszeg: " + str(vegosszeg))
#

def raktarkeszlet_ertek(keszlet, arak) :
    osszertek = 0
    for aru, darab in keszlet.items() :
        osszertek += darab * arak[aru]
    return osszertek
#

def main() :
    
    keszlet =   {
                    "banan": 6,
                    "alma": 31,
                    "narancs": 32,
                    "korte": 15
                }
    
    arak =  {
                "banan": 100,
                "alma": 80,
                "narancs": 120,
                "korte": 90
            }
    
    # 1. feladat:
    #vasarlas(keszlet, arak)
    
    # 2. feladat:
    print("Az osszes aru erteke:")
    
    osszertek = raktarkeszlet_ertek(keszlet, arak)
    assert (osszertek == 6 * 100 + 31 * 80 + 32 * 120 + 15 * 90)
    print(osszertek)
    
    
#



if __name__ == "__main__" :
    main()
#