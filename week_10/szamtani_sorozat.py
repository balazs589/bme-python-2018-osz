
# -----------------------------------------------------------------------------
# import:


# -----------------------------------------------------------------------------
# fuggvenyek:

def szamtani_sorozat_eleme(a, d, i) :
    """
    Rekurziv fuggveny, ami kiszamolja egy szamtani sorozat i.-edik elemet.
    
    Parameterek
    -----------
    a : float
        A szamtani sorozat elso tagja.
    d : float
        A szamtani sorozat novekmenye.
    i : int
        A szamtani sorozat hanyadik elemere vagyunk kivancsiak.
        
    Visszateresi ertek
    ------------------
    S_i : float
        A szamtani sorozat i.-edik eleme.
        
    """
    if i == 1 :
        return a
    else :
        return szamtani_sorozat_eleme(a, d, i - 1) + d
    
#


def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    a = 1.0
    d = 3.0
    for i in range(1, 11) :
        print("S{} = {}".format(i, szamtani_sorozat_eleme(a, d, i)))
    
    
    print(                         elvalaszto_sor                         )
    
    
#

# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#

