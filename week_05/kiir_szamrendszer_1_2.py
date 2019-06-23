

# -----------------------------------------------------------------------------
# szamjegy erteket nagyobb alapu szamrendszerbeli szamjeggye konvertalo fuggveny

def nagyobb_alap(szamjegy_ertek) :      # 36-os szamrendszerig bezarolag van ABC
    if szamjegy_ertek > 9 :
        szamjegy = chr(55+szamjegy_ertek)
    else :
        szamjegy = str(szamjegy_ertek)
    return szamjegy
#

# -----------------------------------------------------------------------------
# szamerteket adott alapu szamrendszerbeli szamjegyekke konvertalo fuggveny:

def szamjegyek(ertek, szamrendszer) :
    ciklus_ertek = ertek
    while ciklus_ertek != 0 :
        szamjegy_ertek = ciklus_ertek % szamrendszer
        szamjegy = nagyobb_alap(szamjegy_ertek)
        szamjegy_lista.insert(0, szamjegy)
        ciklus_ertek //= szamrendszer
    #
    return szamjegy_lista

# -----------------------------------------------------------------------------
# ertek = -10
# szamrendszer = 16   # max 36-os szamrendszerig!


# program futtatasa:

# bekerjuk a szamerteket es az uj szamrendszer alapjat:
while True:
    try:
        ertek = int(input("\nA szam erteke 10-es szamrendszerben:" ))
        szamrendszer = int(input("\nSzamrendszer alapja ( 2 - 36 kozotti egesz ertek):" ))
        if szamrendszer < 2 or szamrendszer > 36 :
            raise Exception("A szamrendszer alapja csak 2 es 36 kozotti egesz ertek lehet!")
        break
    except Exception as e:
        print("Hiba:", e)
#

print()
szamjegy_lista = []

# pozitiv vagy 0 vagy negativ ertekekre is mukodik:
if ertek > 0 :
    szamjegy_lista = szamjegyek(ertek, szamrendszer)
    szam = "".join(szamjegy_lista)
elif ertek == 0 :
    szam = "0"
else :
    szamjegy_lista = szamjegyek( (-1)*ertek, szamrendszer)
    szam = "-" + "".join(szamjegy_lista)
#


print("-" * 79)
print("A megadott ertek 10 alapu szamrendszerben: {}".format(ertek))
print("A megadott ertek {} alapu szamrendszerben: {}".format(szamrendszer, szam))
print("-" * 79)




