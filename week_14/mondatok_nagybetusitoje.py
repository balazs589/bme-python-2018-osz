
"""
                |            beolvasott karakter              |
+---------------+--------------+--------------+---------------+
|               |   "space"    | "mondatzaro" |      "betu"   |
+===============+==============+==============+===============+
| ELEJE         |  -> ELEJE    | -> ELEJE     | -> KOZEPE     |
|               |   print(c)   |  print(c)    |    uppercase  |
+---------------+--------------+--------------+---------------+
| KOZEPE        |  -> KOZEPE   |    -> VEGE   | -> KOZEPE     |
|               |   print(c)   |  print(c)    |   print(c)    |
+---------------+--------------+--------------+---------------+
| VEGE          |  -> ELEJE    |   -> VEGE    |    -> KOZEPE    |
|               |   print(c)   |  print(c)    |   print(c)    |
+---------------+--------------+--------------+---------------+

"""

# -----------------------------------------------------------------------------
import sys

# -----------------------------------------------------------------------------
# allapotok:
# allapottablazat sorai

ELEJE   = 0
KOZEPE  = 1
VEGE    = 2

hanyadik = 0

# muveletek:
def f0(c) :
    sys.stdout.write(c)
#
def f1(c) :
    sys.stdout.write(c.upper())     # karakterkodolastol fugoen nem biztos, hogy az ekezetes betukre is mukodik
#

def karakterosztaly(c) :
    # allapotgep oszlopai
    if      c == " " or c == "\n"               : return 0
    elif    c == "." or c == "!" or c == "?"    : return 1
    else                                        : return 2

allapotgep = [
                [(ELEJE,  f0),  (ELEJE, f0),  (KOZEPE, f1)], 
                [(KOZEPE, f0),  (VEGE,  f0),  (KOZEPE, f0)], 
                [(ELEJE,  f0),  (VEGE,  f0),  (KOZEPE, f0)], 
                                                                                ]

# -----------------------------------------------------------------------------

def allapotgeppel() :
    
    allapot = ELEJE
    
    while True :
        
        c = sys.stdin.read(1)
        
        if c == "" :
            break
        
        esemeny = karakterosztaly(c)
        ujallapot, muvelet = allapotgep[allapot][esemeny]
        muvelet(c)
        allapot = ujallapot
        
#


# -----------------------------------------------------------------------------

def main() :
    
    allapotgeppel()
#

# -----------------------------------------------------------------------------
if __name__ == "__main__" :
    main()
#

