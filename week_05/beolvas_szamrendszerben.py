


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


while True:
    try:
        print("Hanyas szamrendszerben fogsz irni?")
        szamrendszer = int(input())
        print("Ird be a szamot!")
        szam = input()
        
        if szamrendszer < 2 or szamrendszer > 36 :  # 36-os szamrendszerig bezarolag mukodik
            raise Exception("A szamrendszer alapja csak 2 es 36 kozotti egesz ertek lehet!")
        
        if not szam.isalnum() :
            raise Exception("A szam csak szamjegyekbol es az angol abc betuibol allhatnak!")
        
        for szamjegy in szam :
            if szamjegy_ertek(szamjegy) >= szamrendszer :
                raise Exception("A szam a szamrendszernek nem megfelelo karaktert is tartalmaz!")
        
        break
        
    except Exception as e:
        print("Hiba:", e)
#

szamertek = szam_erteke(szam, szamrendszer)

print("-" * 79)
print()
print("A beolvasott szam 10-es szamrendszerben:", szamertek)
print("Ellenorzes beepitett megoldassal:       ", int(szam, szamrendszer))
print()



