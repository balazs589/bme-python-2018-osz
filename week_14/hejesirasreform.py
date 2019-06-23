"""

ly -> j
lly -> jj

allapotatmeneti tabla:

                |                    beolvasott karakter                     |
+---------------+---------------+--------------+--------------+--------------+
|               |      "l"      |      "y"     | "egyeb betu" | "fajl vege"  |
+===============+===============+==============+==============+==============+
| ALAP          | -> L_VOLT     |    -> ALAP   |    -> ALAP   |  -> KILEP    |
|               |               |  print(y)    | print(betu)  |              |
+---------------+---------------+--------------+--------------+--------------+
| L_VOLT        | -> LL_VOLT    |    -> ALAP   |    -> ALAP   |  -> KILEP    |
|               |               |  print(j)    |print(l,betu) |    print(l)  |
+---------------+---------------+--------------+--------------+--------------+
| LL_VOLT       | -> LL_VOLT    |    -> ALAP   |    -> ALAP   |  -> KILEP    |
|               |  print(l)     |  print(jj)   |print(ll,betu)|   print(ll)  |
+---------------+---------------+--------------+--------------+--------------+
| KILEP         |           osszevonva: kilepes minden esetben               |
+---------------+---------------+--------------+--------------+--------------+

"""

# -----------------------------------------------------------------------------
import sys

# -----------------------------------------------------------------------------
# allapotok:
# allapottablazat sorai ( + KILEP)

ALAP        = 0
L_VOLT      = 1
LL_VOLT     = 2
KILEP       = 3


# muveletek:
def f0(c) :
    sys.stdout.write("")
#
def f1(c) :
    sys.stdout.write("y")
#
def f2(c) :
    sys.stdout.write(c)
#
def f3(c) :
    sys.stdout.write("j")
#
def f4(c) :
    sys.stdout.write("l" + c)
#
def f5(c) :
    sys.stdout.write("l")
#
def f6(c) :
    sys.stdout.write("jj")
#
def f7(c) :
    sys.stdout.write("ll" + c)
#
def f8(c) :
    sys.stdout.write("ll")
#


def karakterosztaly(karakter) :              # kis es nagybetukkel is
    # allapotgep oszlopai
    if      karakter == "l" or karakter == "L"  : return 0
    elif    karakter == "y" or karakter == "Y"  : return 1
    elif    karakter != ""                      : return 2
    else                                        : return 3      # windows: ctrl-Z vagy EOF

allapotgep = [
                [(L_VOLT,  f0),  (ALAP, f1),  (ALAP, f2),  (KILEP, f0)], 
                [(LL_VOLT, f0),  (ALAP, f3),  (ALAP, f4),  (KILEP, f5)], 
                [(LL_VOLT, f5),  (ALAP, f6),  (ALAP, f7),  (KILEP, f8)], 
                                                                                ]   # KILEP-hez tartozo sorban nem lenne muvelet

# -----------------------------------------------------------------------------

def allapotgeppel() :
    
    allapot = ALAP
    
    while True :
        
        c = sys.stdin.read(1)
        esemeny = karakterosztaly(c)
        ujallapot, muvelet = allapotgep[allapot][esemeny]
        muvelet(c)
        allapot = ujallapot
        
        if allapot == KILEP :   #
            break
        
#


# -----------------------------------------------------------------------------

def main() :
    allapotgeppel()
#

# -----------------------------------------------------------------------------
if __name__ == "__main__" :
    main()
#

