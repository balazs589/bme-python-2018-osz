"""
https://infopy.eet.bme.hu/lab06/#8

Adott szamrendszerbeli szamot tartalmazo sztringet kell most ertelmezni. (Lasd a regebbi laborfeladatot.) Peldaul szamrendszerbol("fce2", 16) erteke legyen 64738. Dobj itt is ValueError kivetelt, ha helytelen az alap, vagy helytelen karaktert talalsz a sztringben!

"""



# -----------------------------------------------------------------------------
# 
def szamjegy_ertek(szamjegy) :
    if szamjegy.isnumeric() :
        ertek = int(szamjegy)
    else :
        ertek = ord(szamjegy.upper()) - 55      # kis es nagybetuk egyarant szerepelhetnek
    return ertek
# end szamjegy_ertek



# -----------------------------------------------------------------------------

def szam_erteke(szam, szamrendszer) :
    
    if szamrendszer < 2 or szamrendszer > 36 :
        raise ValueError("A szamrendszer alapja csak 2 es 36 kozotti egesz ertek lehet!")
    
    if not szam.isalnum() :
        raise ValueError("A szam csak szamjegyekbol es az angol abc betuibol allhat!")
    
    for szamjegy in szam :
        if szamjegy_ertek(szamjegy) >= szamrendszer :
            raise ValueError("A szam a szamrendszernek nem megfelelo karaktert is tartalmaz: " + szamjegy)
            
    szamjegy_lista = list(szam)
    szamertek = 0
    hatvany = 0
    while szamjegy_lista != [] :
        szamjegy = szamjegy_lista.pop()
        szamertek += szamjegy_ertek(szamjegy) * szamrendszer ** hatvany
        hatvany += 1
    # end while
    return szamertek
# end szam_erteke


# -----------------------------------------------------------------------------
def main():
    try:
        print("Hanyas szamrendszerben fogsz irni?")
        szamrendszer = int(input())
        print("Ird be a szamot!")
        szam = input()
        
        szamertek = szam_erteke(szam, szamrendszer)
        
        print("-" * 79)
        print()
        print("A beolvasott szam 10-es szamrendszerben:", szamertek)
        print("Ellenorzes beepitett megoldassal:       ", int(szam, szamrendszer))
        print()
        
    except ValueError as e:
        print("ValueError:", e)
    except Exception as e:
        print("Other Exception:", e)
#



# -----------------------------------------------------------------------------

main()