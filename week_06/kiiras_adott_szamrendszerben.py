"""
https://infopy.eet.bme.hu/lab06/#7

Elevenitsd fel a multkori labor kiiras adott szamrendszerben cimu feladatat!

Tedd be most ezt egy fuggvenybe, pl. szamrendszerbe(9, 2) erteke legyen az "1001" sztring! Ha hibas erteket kap a fuggveny (pl. negativ vagy tul nagy alapot), akkor dobjon ValueError kivetelt!

Irj foprogramot, amelyben meghivod a fuggvenyt a felhasznalo altal megadott szamra es alapra! Kapd el a kivetelt, hogy hibajelzest tudja adni! Gyakorlaskepp megirhatod az atalakito fuggvenyt is; ez egyre inkabb rutinbol kell menjen.

"""

# =============================================================================
# import:

# =============================================================================
# fuggvenyek:

# ----------------------------------------------------------------------

def harminchatos_szamrendszer_szerint(szam) :
    """
    Fuggveny ami egy egesz szam erteket egy darab, az ertekenek megfelelo
    36-os szamrendszerbeli szamjeggye konvertal.
    
    Args:
        szam (int): Egesz szam, amit 36-os szamrendszerbe konvertalunk.
       
    Returns:
        string:     A szam 36-os szamrendszerbeli szimboluma, 1 db karakter.
    
    Raises:
        ValueError: Ha nincs a szamerteknek megfelelo 36-os szamrendszerbeli
                    szamjegy, azaz ha szam nem egesz erteku
                    vagy szam nincs benne a [0, 35] intervallumban.
        TypeError:  Ha a bemeno parameter nem konvertalhato egesz szamma.
                    pl. szam = None
    
    Usage:
    
    >>> szamjegy = harminchatos_szamrendszer_szerint(33)
    
    """
    if szam != int(szam) :        # dobhat TypeError-t is
        raise ValueError("A megadott szam nem egesz szam: " + str(szam))
    if szam < 0 or szam > 35 :
        raise ValueError("Nincs 36-os szamrendszerbeli szamjegy ami megfelel a megadott szamnak: " + str(szam))
        
    if szam > 9 :
        szamjegy = chr(55 + szam)
    else :
        szamjegy = str(szam)
    return szamjegy
#

# -----------------------------------------------------------------------------
# 

def szamrendszerbe(szam, szamrendszer) :
    """
    Egy szamot adott alapu szamrendszerbe konvertalo fuggveny.
    
    Args:
        szam (int): Egesz szamertek, aminek szamjegyeit "szamrendszer"
                    szamrendszerben hatarozzuk meg.
       
    Returns:
        string:     A szam adott szamrendszerbeli alakja, betuk eseten nagybetuk.
    
    Raises:
        ValueError: Ha szam nem egesz vagy negativ, illetve
                    ha szamrendszer nem egesz erteku
                    vagy nincs benne a [2, 36] intervallumban.
        TypeError:  Ha a bemeno parameterek legalabb egyike nem konvertalhato egesz szamma.
                    pl. szam = None
    
    Usage:
    
    >>> szamjegy = szamrendszerbe(szam=33, szamrendszer=36)
    
    """
    if szam != int(szam) :                          # dobhat TypeError-t is
        raise ValueError("A megadott szam nem egesz szam: " + str(szam))
    if szamrendszer != int(szamrendszer) :          # dobhat TypeError-t is
        raise ValueError("A szamrendszer alapja nem egesz szam: " + str(szamrendszer))
    if szam < 0 :
        raise ValueError("A konvertalas csak pozitiv szamra vegezheto el, a megadott szam: " + str(szam))
    if szamrendszer < 2 or szamrendszer > 36 :
        raise ValueError("A szamrendszer alapja csak a [2, 36] zart intervallumon levo egesz szam lehet, a megadott ertek: " + str(szamrendszer))
    
    szamjegy_lista = []
    
    while szam != 0 :
        szamjegy_ertek = szam % szamrendszer
        szamjegy = harminchatos_szamrendszer_szerint(szamjegy_ertek)
        szamjegy_lista.insert(0, szamjegy)
        szam //= szamrendszer
    #
    return "".join(szamjegy_lista)
#



# ----------------------------------------------------------------------
def main() :
    
    while True:
        try:
            print("-" * 79)
            szam = int(input("\nA szam erteke 10-es szamrendszerben:" ))
            szamrendszer = int(input("\nSzamrendszer alapja ( 2 - 36 kozotti egesz ertek):" ))
            szam_konvertalva = szamrendszerbe(szam, szamrendszer)
            
            print("-" * 79)
            print("A megadott ertek 10 alapu szamrendszerben: {}".format(szam))
            print("A megadott ertek {} alapu szamrendszerben: {}".format(szamrendszer, szam_konvertalva))
            print("-" * 79)
            
            break
        except TypeError as e:
            print("\nSikertelen konvertalas.")
            print("Hiba:", e)
        except ValueError as e:
            print("\nA szamitas nem vegezheto el a megadott ertekekkel.")
            print("Hiba:", e)
    # end while
# end main


# =============================================================================
# futtatas:


main()
exit()








# gyakorlas:
# =============================================================================

"""

# =============================================================================
# https://colab.research.google.com/drive/1zuHMo3Z1G66UOOGdEw5mdbEaICicqJiS
# https://docs.python.org/3/library/unittest.html

import unittest
    
#@unittest.SkipTest
class Test(unittest.TestCase):
    
#          1         2         3     
#01234567890123456789012345678901234567890
#0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    def test_00(self):
        szam = 0
        print("\n test_00:\nszam={}".format(szam))
        szamjegy = harminchatos_szamrendszer_szerint(szam)
        print(szamjegy)
        self.assertEqual("0", szamjegy)
    
    def test_05(self):
        szam = 5
        print("\n test_05:\nszam={}".format(szam))
        szamjegy = harminchatos_szamrendszer_szerint(szam)
        print(szamjegy)
        self.assertEqual("5", szamjegy)
    
    def test_12(self):
        szam = 12
        print("\n test_12:\nszam={}".format(szam))
        szamjegy = harminchatos_szamrendszer_szerint(szam)
        print(szamjegy)
        self.assertEqual("C", szamjegy)
    
    def test_32(self):
        szam = 32
        print("\n test_32:\nszam={}".format(szam))
        szamjegy = harminchatos_szamrendszer_szerint(szam)
        print(szamjegy)
        self.assertEqual("W", szamjegy)
    
    def test_42(self):
        szam = 42
        print("\n test_42:\nszam={}".format(szam))
        #szamjegy = harminchatos_szamrendszer_szerint(szam)
        #print(szamjegy)
        self.assertRaises(ValueError, harminchatos_szamrendszer_szerint, szam)
    
    def test_52(self):
        szam = 52
        print("\n test_52:\nszam={}".format(szam))
        regex  = "Nincs 36-os szamrendszerbeli szamjegy ami megfelel a megadott szamnak: .*$" # + str(szam)
        self.assertRaisesRegex(ValueError, regex, harminchatos_szamrendszer_szerint, szam)
    
    def test_52_negativ(self):
        szam = -52
        print("\n test_52:\nszam={}".format(szam))
        regex  = "Nincs 36-os szamrendszerbeli szamjegy ami megfelel a megadott szamnak: .*$" # + str(szam)
        self.assertRaisesRegex(ValueError, regex, harminchatos_szamrendszer_szerint, szam)
#


def unit_test() :
    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
# end unit_test

unit_test()
"""



"""
# pozitiv vagy 0 vagy negativ ertekekre...
if ertek > 0 :
    szamjegy_lista = szamrendszerbe(ertek, szamrendszer)
    szam = "".join(szamjegy_lista)
elif ertek == 0 :
    szam = "0"
else :
    szamjegy_lista = szamrendszerbe( (-1)*ertek, szamrendszer)
    szam = "-" + "".join(szamjegy_lista)
#
"""



