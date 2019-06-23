
# =============================================================================
# import:


# =============================================================================
# osztalyok, fuggvenyek:

# -----------------------------------------------------------------------------

class Idopont:
    def __init__(self, ora, perc) :
        self.ora = ora
        self.perc = perc
    
    def __str__(self) :
        return "{:02}:{:02}".format(self.ora, self.perc)
    
    def __add__(self, p) :
        perc = self.perc + p
        ora = (self.ora + perc // 60) % 24
        perc %= 60
        return Idopont(ora, perc)
    
    def __sub__(self, p) :
        if type(p) is Idopont :
            return (self.ora - p.ora) * 60 + (self.perc - p.perc)
        if type(p) is int :
            perc = self.perc - p
            ora = (self.ora + perc // 60) % 24
            perc %= 60
            return Idopont(ora, perc)
#

# -----------------------------------------------------------------------------
def ido_kiir(i) :
    return "{:02}:{:02}".format(i.ora, i.perc)
#

# -----------------------------------------------------------------------------
def ido_hozzaad(i, p) :
    perc = i.perc + p
    ora = (i.ora + perc // 60) % 24
    perc %= 60
    
    return Idopont(ora, perc)
#

# -----------------------------------------------------------------------------
def ido_eltelt(i1, i2) :
    return (i1.ora - i2.ora) * 60 + (i1.perc - i2.perc)
#

# -----------------------------------------------------------------------------
def ido_kivon(i, p) :
    perc = i.perc - p
    ora = (i.ora + perc // 60) % 24
    perc %= 60
    
    return Idopont(ora, perc)
#



# -----------------------------------------------------------------------------

def main():
    ido = Idopont(23, 30)
    
    print(ido_kiir(ido))
    print(ido_kiir(ido_hozzaad(ido, 40)))
    
    ido1 = Idopont(17, 30)
    ido2 = Idopont(10, 30)
    print(ido_eltelt(ido1, ido2))
    
    ido3 = Idopont(0, 30)
    print(ido_kiir(ido_kivon(ido3, 40)))
    
    
    print("-" * 79)
    
    print(ido)
    print(ido + 40)
    print(ido1 - ido2)
    print(ido3 - 40)
    
#


# =============================================================================
# futtatas:


main()









