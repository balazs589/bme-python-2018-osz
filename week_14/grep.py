"""

"""

# -----------------------------------------------------------------------------
import re

# -----------------------------------------------------------------------------

def grep() :
    
    print("Adj meg egy regularis kifejezest!")
    regex = input()
    
    with open("szavak.txt", "rt", encoding="utf-8") as f:
        for sor in f:
            sor = sor.rstrip("\n")
            if re.search(regex, sor) :
                print(sor)
    
#

"""
Adj meg regularis kifejezeseket, amelyekkel kilistazhatod az alabbi szavakat:

    Amelyekben van vicc (pl. vicces, de kaviccsal is)           r"vicc"
    Almaval kezdodnek (pl. almaecet, de siman alma is)          r"^alma"
    Ugy vegzodnek, hogy hely (pl. taborhely, zabpehely)         r"hely$"
    Negy betusek, es mindket kozepso betujuk n (pl. enni).      r"^.nn.$"
    Hat betusek, fru-val kezdodnek (pl. fruska).                r"^fru.{3}$"
    Hosszu o-val kezdodo es vegzodo szavak (pl. oceanjaro).     r"^o.*o$"
    Ket hosszu ssz szerepel bennuk (pl. osszevisszasag).        r"ssz.*ssz"
    Szerepel bennuk ketszer ugyanaz a negybetus reszlet         r"(.{4}).*\1"
            (pl. tisztiszolga, rendszerszeru)                   
    Hat betubol allnak, ketszer ugyanaz (pl. bonbon)            r"^(.{3})\1$"
    Hatbetus tukorszavak (pl. lappal)                           r"^(.)(.)(.)\3\2\1$"
    Hetbetus tukorszavak (pl. talalat)                          r"^(.)(.)(.).\3\2\1$"
"""




# -----------------------------------------------------------------------------

def main() :
    grep()
#

# -----------------------------------------------------------------------------
if __name__ == "__main__" :
    main()
#

