"""

"""

# =============================================================================

# -----------------------------------------------------------------------------
def szokoev(evszam) :
    """Fuggveny ami megmondja, hogy egy ev szokoev-e.
    
    Args:
        evszam (int): Pozitiv egesz szam.
       
    Returns:
        bool:
            True:  ha az adott evszam szokoevhez tartozik
            False: ha az adott evszam nem szokoevhez tartozik
    Hasznalat:
    
    >>> febr29 = szokoev(2017)
    >>> febr29 = szokoev(2018)
    >>> febr29 = szokoev(2019)
    """
    
#    ???
#    try:
#        evszam = int(evszam)
#    except ValueError as e:
#        print("Hiba:", e)      ???
#        return None            ???
#    if evszam <= 0 :
#        print("A fuggveny csak idoszamitas utani evekre mukodik!")     ???
#        return None            ???
    
    if evszam % 400 == 0 :
        return True
    if evszam % 100 == 0 :
        return False
    if evszam % 4 == 0 :
        return True
        
    return False
# end szokoev


# -----------------------------------------------------------------------------
def main() :
    """
    Feladat megoldasa.
    """
    while True :
        print("Adj meg egy pozitiv egesz evszamot!")
        try:
            evszam = int(input("? "))
            if evszam > 0 :
                break
        except:
            pass
    #
    if szokoev(evszam) :
        print("Szokoev.")
    else :
        print("Nem szokoev.")
    
# end main

# =============================================================================


main()



