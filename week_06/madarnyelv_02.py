"""
https://infopy.eet.bme.hu/lab06/#9


"""
# =============================================================================
# import :

# =============================================================================
# fuggvenyek:


# -----------------------------------------------------------------------------
def maganhangzo(karakter) :
    return True if karakter in "aaeeiioooouuuuAAEEIIOOOOUUUU" else False
#

# -----------------------------------------------------------------------------
def madarnyelv(eredeti_szoveg) :
    uj_szoveg = ""
    for c in eredeti_szoveg :
        if maganhangzo(c) :
            uj_szoveg += (c + "v" + c.lower())
        else :
            uj_szoveg += c
    return uj_szoveg
#



# -----------------------------------------------------------------------------
def main() :
    print("-" * 79)
    
    print("Irj be egy sornyi szoveget enterrel lezarva!")
    szoveg = input()
    print(madarnyelv(szoveg))
    
    print("-" * 79)
    
    
#

# =============================================================================
# futtatas:

main()

# =============================================================================



"""

# gyakorlas:
# =============================================================================



# =============================================================================
# https://colab.research.google.com/drive/1zuHMo3Z1G66UOOGdEw5mdbEaICicqJiS
# https://docs.python.org/3/library/unittest.html

import unittest
    
#@unittest.SkipTest
class Test(unittest.TestCase):
    
    def test_01(self):
        eredeti_szoveg = "madarnyelven"
        print("\n test_01:\n eredeti_szoveg={}".format(eredeti_szoveg))
        uj_szoveg = madarnyelv(eredeti_szoveg)
        print(uj_szoveg)
        self.assertEqual("mavadavarnyevelveven", uj_szoveg)
    
    def test_alma(self):
        eredeti_szoveg = "alma"
        print("\n test_alma:\n eredeti_szoveg={}".format(eredeti_szoveg))
        uj_szoveg = madarnyelv(eredeti_szoveg)
        print(uj_szoveg)
        self.assertEqual("avalmava", uj_szoveg)
    
    def test_Alma(self):
        eredeti_szoveg = "Alma"
        print("\n test_Alma:\n eredeti_szoveg={}".format(eredeti_szoveg))
        uj_szoveg = madarnyelv(eredeti_szoveg)
        print(uj_szoveg)
        self.assertEqual("Avalmava", uj_szoveg)
    
#

def unit_test() :
    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
# end unit_test

unit_test()

"""

