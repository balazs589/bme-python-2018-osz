"""
"""

# -----------------------------------------------------------------------------
# import:

import keretprogram as binfa

# -----------------------------------------------------------------------------
# fuggvenyek:

def kiir(gyoker) :
    if gyoker is None :
        return
    
    kiir(gyoker.bal)
    print(gyoker.ertek, end=" ")
    kiir(gyoker.jobb)
#


def main() :
    
    tesztadat = [15, 96, 34, 12, 14, 56, 21, 11, 10, 9, 78, 43]
    gyoker = None
    for x in tesztadat:
        gyoker = binfa.beszur(gyoker, x)
    
    
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    kiir(gyoker)
    
    print(                         elvalaszto_sor                         )
    
#


# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#