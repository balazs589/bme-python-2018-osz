"""
https://infopy.eet.bme.hu/lab06/#4

Egy olyan fuggvenyt kell irnod, amely parameterkent sztringek listajat kapja. Meg kell vizsgalnia a listaban talalhato sztringeket, es megvalaszolnia ezt a kerdest: van-e olyan sztring, amelyik „a” betuvel kezdodik! Ennek is legyen logikai tipusu a visszateresi erteke.

Feladat megoldasa, docstring es unittest gyakorlas.
"""

# =============================================================================
import unittest

# =============================================================================

# ----------------------------------------------------------------------
def fuggveny(sztring_lista) :
    """
    A fuggveny eldonti, hogy van-e olyan sztring a parameterkent megkapott listaban, ami "a" karkaterrel kezdodik.
    
    Args:
        sztring_lista (list): Vizsgalni kivant sztringek listaja.
       
    Returns:
        bool:
            True:  ha van olyan sztring a listaban, ami "a" betuvel kezdodik
            False: ha nincs olyan sztring a listaban, ami "a" betuvel kezdodik
    Hasznalat:
    
    >>> van_a = fuggveny(["apple", "", "orange"])
    """
    
    if sztring_lista == [] :
        if verbose :
            print("Result: Ures lista.")
        return False
    for szo in sztring_lista :
        if len(szo) > 0 and szo[0] == "a" :
            if verbose :
                print("Result: Elso olyan szo ami \"a\" betuvel kezdodik: \"{}\".".format(szo))
            return True
    if verbose :
        print("Result: Nincs \"a\" betuvel kezdodo szo.")
    return False
# end fuggveny




# =============================================================================
# https://colab.research.google.com/drive/1zuHMo3Z1G66UOOGdEw5mdbEaICicqJiS

verbose = True
#verbose = False
#@unittest.SkipTest
class Test(unittest.TestCase):
    
    
    def test_van_aval_kezdodo(self):
        sztring_lista = ["korte", "alma", "barack"]
        print("\ntest_van_aval_kezdodo:\nsztring_lista={}".format(sztring_lista))
        van_a = fuggveny(sztring_lista)
        self.assertEqual(True, van_a)
    
    def test_nincs_aval_kezdodo(self):
        sztring_lista = ["dinnye", "papaja", "", "zeller"]
        print("\ntest_nincs_aval_kezdodo:\nsztring_lista={}".format(sztring_lista))
        van_a = fuggveny(sztring_lista)
        self.assertEqual(False, van_a)
    
    def test_ures_lista(self):
        sztring_lista = []
        print("\ntest_ures_lista:\nsztring_lista={}".format(sztring_lista))
        van_a = fuggveny(sztring_lista)
        self.assertEqual(False, van_a)
#

def unit_test() :
    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
# end unit_test


# =============================================================================

# ----------------------------------------------------------------------
def main() :
    #sztring_lista = ["korte", "alma", "barack"]
    #sztring_lista = ["dinnye", "papaja", "", "zeller"]
    sztring_lista = []
    
    print()
    print(sztring_lista)
    
    van_a = fuggveny(sztring_lista)
    
    if van_a :
        print("\nVan \"a\" betuvel kezdodo szo.\n")
    else :
        print("\nNincs \"a\" betuvel kezdodo szo.\n")
# end main


# =============================================================================

unit_test()
#main()