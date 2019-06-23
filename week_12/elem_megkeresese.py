"""
"""

# -----------------------------------------------------------------------------
# import:

import keretprogram as binfa
import fa_kiirasa


# -----------------------------------------------------------------------------
# fuggvenyek:


def elemet_keres_rekurzioval(gyoker, ertek) :       # rekurziv
    #print(gyoker.ertek)
    
    if gyoker is not None and gyoker.ertek != ertek :
        
        if ertek < gyoker.ertek :
            return elemet_keres_rekurzioval(gyoker.bal, ertek)
        elif ertek > gyoker.ertek :
            return elemet_keres_rekurzioval(gyoker.jobb, ertek)
    
    return gyoker
    
#


def elemet_keres_iteracioval(gyoker, ertek) :
    mozgo = gyoker
    
    while mozgo is not None and mozgo.ertek != ertek :
        #print(mozgo.ertek)
        
        if ertek < mozgo.ertek :
            mozgo = mozgo.bal
        elif ertek > mozgo.ertek :
            mozgo = mozgo.jobb
    
    return mozgo
    
#


def main() :
    
    tesztadat = [15, 96, 34, 12, 14, 56, 21, 11, 10, 9, 78, 43]
    gyoker = None
    for x in tesztadat:
        gyoker = binfa.beszur(gyoker, x)
    
    print()
    fa_kiirasa.kiir(gyoker)
    
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    # benne van:
    talalat = elemet_keres_rekurzioval(gyoker, 21)
    assert (talalat is not None)
    print("talalat.ertek =", talalat.ertek)
    
    print(                         elvalaszto_sor                         )
    
    # nincs benne:
    talalat = elemet_keres_rekurzioval(gyoker, 19)
    assert (talalat is None)
    
    print(                         elvalaszto_sor                         )
    
    # benne van iteracioval:
    talalat = elemet_keres_iteracioval(gyoker, 21)
    assert (talalat is not None)
    print("talalat.ertek =", talalat.ertek)
        
    print(                         elvalaszto_sor                         )
    
    # nincs benne:
    talalat = elemet_keres_iteracioval(gyoker, 19)
    assert (talalat is None)
        
    print(                         elvalaszto_sor                         )
    
#


# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#