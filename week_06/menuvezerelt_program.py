"""
https://infopy.eet.bme.hu/lab06/#6


"""

# =============================================================================
# import:

# =============================================================================
# fuggvenyek:

# ----------------------------------------------------------------------
def alapertek_visszaallitasa(a) :
    return 1
#

# ----------------------------------------------------------------------
def hozzaad_egyet(a) :
    return a + 1
#

# ----------------------------------------------------------------------
def elojelet_valtoztat(a) :
    return (-1) * a
#

# ----------------------------------------------------------------------
def megszorozza_kettovel(a) :
    return 2 * a
#

# ----------------------------------------------------------------------
def muvelet(a, valasz) :
    menu_opciok = [0, 1, 2, 3, 9]
    if valasz == menu_opciok[0] :
        return alapertek_visszaallitasa(a)
    if valasz == menu_opciok[1] :
        return hozzaad_egyet(a)
    if valasz == menu_opciok[2] :
        return elojelet_valtoztat(a)
    if valasz == menu_opciok[3] :
        return megszorozza_kettovel(a)
# end muvelet


def hibas_input() :
    print("Nincs ilyen menupont!")
#


# ----------------------------------------------------------------------
def main() :
    a = 1
    
    valasz = 0
    menu_opciok = [0, 1, 2, 3, 9]
    
    while valasz != 9 :
        print("-" * 79)
        print("a = {}".format(a), end="\n\n")
        print(  "0. Alapertek visszaallitasa (a = 1)",
                "1. Hozzaad 1-et",
                "2. Megforditja az elojelet",
                "3. Szorozza 2-vel",
                "9. Kilepes",
                sep="\n",
                end=("\n" + "-" * 79 + "\n\n"))
        try :
            valasz = int(input("Muvelet: "))
            if valasz not in menu_opciok :
                hibas_input()
                continue
            a = muvelet(a, valasz)
        except Exception as e :
            hibas_input()
    # end while
# end main


# =============================================================================
# futtatas:


main()