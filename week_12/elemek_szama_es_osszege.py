"""
"""

# -----------------------------------------------------------------------------
# import:

import keretprogram as binfa

# -----------------------------------------------------------------------------
# fuggvenyek:

def elemek_szama(gyoker) :
    if gyoker is None :
        return 0
    
    return elemek_szama(gyoker.bal) + elemek_szama(gyoker.jobb) + 1
#

def elemek_osszege(gyoker) :
    if gyoker is None :
        return 0
    
    return elemek_osszege(gyoker.bal) + elemek_osszege(gyoker.jobb) + gyoker.ertek
    
#


def main() :
    
    tesztadat = [15, 96, 34, 12, 14, 56, 21, 11, 10, 9, 78, 43]
    gyoker = None
    for x in tesztadat:
        gyoker = binfa.beszur(gyoker, x)
    
    
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    elemszam = elemek_szama(gyoker)
    
    assert (elemszam == len(tesztadat))
    print("elemek szama:", elemszam)
    
    print(                         elvalaszto_sor                         )
    
    elemosszeg = elemek_osszege(gyoker)
    
    assert (elemosszeg == sum(tesztadat))
    print("elemek osszege:", elemosszeg)
    
    
    print(                         elvalaszto_sor                         )
    
#


# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#