"""

ly -> j
lly -> jj
Ly -> J

mast nem cserel


allapotatmeneti tabla:

                |                    beolvasott karakter                     |
+---------------+---------------+---------------+--------------+--------------+--------------+
|               |      "L"      |      "l"      |      "y"     | "egyeb betu" | "fajl vege"  |
+===============+===============+===============+==============+==============+==============+
| ALAP          | -> NAGY_L_VOLT| -> L_VOLT     |    -> ALAP   |    -> ALAP   |  -> KILEP    |
|               |               |               |  print(y)    | print(betu)  |              |
+---------------+---------------+---------------+--------------+--------------+--------------+
| L_VOLT        | -> LL_VOLT    | -> LL_VOLT    |    -> ALAP   |    -> ALAP   |  -> KILEP    |
|               |               |               |  print(j)    |print(l,betu) |    print(l)  |
+---------------+---------------+---------------+--------------+--------------+--------------+
| LL_VOLT       | -> LL_VOLT    | -> LL_VOLT    |    -> ALAP   |    -> ALAP   |  -> KILEP    |
|               |  print(l)     |  print(l)     |  print(jj)   |print(ll,betu)|   print(ll)  |
+---------------+---------------+---------------+--------------+--------------+--------------+
| NAGY_L_VOLT   |-> NAGY_L_VOLT |  ->  L_VOLT   |    -> ALAP   |    -> ALAP   |  -> KILEP    |
|               |   print(L)    |   print(L)    |  print(J)    |print(L,betu) |    print(L)  |
+---------------+---------------+---------------+--------------+--------------+--------------+
| KILEP         |           osszevonva: kilepes minden esetben                               |
+---------------+---------------+---------------+--------------+--------------+--------------+

"""

# -----------------------------------------------------------------------------
import sys

# -----------------------------------------------------------------------------
# allapotok:
# allapottablazat sorai ( + KILEP)

ALAP        = 0
L_VOLT      = 1
LL_VOLT     = 2
NAGY_L_VOLT = 3
KILEP       = 4


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
def f9(c) :
    sys.stdout.write("J")
#
def f10(c) :
    sys.stdout.write("L" + c)
#
def f11(c) :
    sys.stdout.write("L")
#


def karakterosztaly(karakter) :              # kis es nagybetukkel is
    # allapotgep oszlopai
    if      karakter == "L"                     : return 0
    elif    karakter == "l"                     : return 1
    elif    karakter == "y" or karakter == "Y"  : return 2
    elif    karakter != ""                      : return 3
    else                                        : return 4      # windows: ctrl-Z vagy EOF

allapotgep = [
                [(NAGY_L_VOLT,   f0), (L_VOLT,   f0),  (ALAP, f1),  (ALAP,  f2),  (KILEP,  f0)], 
                [(LL_VOLT,       f0), (LL_VOLT,  f0),  (ALAP, f3),  (ALAP,  f4),  (KILEP,  f5)], 
                [(LL_VOLT,       f5), (LL_VOLT,  f5),  (ALAP, f6),  (ALAP,  f7),  (KILEP,  f8)], 
                [(NAGY_L_VOLT,  f11), (L_VOLT,  f11),  (ALAP, f9),  (ALAP, f10),  (KILEP, f11)], 
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

