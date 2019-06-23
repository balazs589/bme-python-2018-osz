"""
"""

# =============================================================================
# import:


# =============================================================================
# fuggvenyek:

# ----------------------------------------------------------------------
def atlagszamitas(szamok) :
    """
    Fuggveny ami meghatarozza a listakent megkapott szamok atlagat.
    """
    szum = 0
    db = 0
    for x in szamok:
        szum += x
        db += 1
    atlag = szum / db
    return atlag
#


# ----------------------------------------------------------------------
def szures(szamok) :
    """
    Fuggveny ami kiszuri a listakent megkapott szamok kozul
    a lista atlaganal kisebb ertekeket.
    """
    atlag = atlagszamitas(szamok)
    szurt = []
    for x in szamok:
        if x < atlag:
            szurt.append(x)
    
    return szurt
#


# ----------------------------------------------------------------------
def main() :
    
    print("-" * 79)
    szamok = [24, 31, 22, 43, 10, 84, 38, 44, 84, 56, 67, 51, 56, 84, 31, 65, 69, 83, 39]
    print(szamok)
    
    szurt = szures(szamok)
    print(szurt)
    print("-" * 79)
    
#


"""
# =============================================================================
import unittest

# @unittest.SkipTest
class Test(unittest.TestCase):
    
    def test_01_mind_egyforma(self):
        szamok = [1, 1, 1, 1, 1, 1]
        print("\ntest_01_mind_egyforma:\nszamok=\t{}".format(szamok))
        szurt = szures(szamok)
        print("szurt=\t{}".format(szurt))
        self.assertEqual([], szurt)
    
    def test_02_fele_kicsi(self):
        szamok = [1, 1, 1, 2, 2, 2]
        print("\ntest_02_mind_egyforma:\nszamok=\t{}".format(szamok))
        szurt = szures(szamok)
        print("szurt=\t{}".format(szurt))
        self.assertEqual([1, 1, 1], szurt)
#

def unit_test() :
    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
# end unit_test

"""

# =============================================================================
# futtatas:

#unit_test()
main()
