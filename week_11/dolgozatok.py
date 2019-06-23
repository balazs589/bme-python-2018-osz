"""

"""

# -----------------------------------------------------------------------------
# import:
import copy

# -----------------------------------------------------------------------------
# osztalyok :

class Eredmeny :
    def __init__(self, nev, neptun, pontszam) :
        self.nev        = nev               # str
        self.neptun     = neptun            # str
        self.pontszam   = pontszam          # int
    
    # teszteleshez:
    def __str__(self) :
        return "{} | {:15} | {:3}".format(self.neptun, self.nev, self.pontszam)
    
    # gyakorlashoz (deepcopy ellenorzesehez):
    def __eq__(self, other) :
        return self.nev == other.nev and self.neptun == other.neptun and self.pontszam == other.pontszam
#

# -----------------------------------------------------------------------------
# fuggvenyek:

# elozo feladatokbol felhasznalva, csak a feldolgozo resz modositva:
def beolvas(input_file) :
    eredmenyek = []
    
    with open(input_file, "rt", encoding="utf-8") as f :
        while True :
            sor = f.readline()
            if sor != "" :
                eredmenyek.append(sort_feldolgoz(sor.rstrip("\n")))     # ez ami uj
            else :
                break
    
    return eredmenyek
#

# eredmeny objektum letrehozasa:
def sort_feldolgoz(sor) :
    adattagok = sor.split(":")
    eredmeny = Eredmeny(adattagok[1], adattagok[0], int(adattagok[2]))
    return eredmeny
    
#

# oszlopdiagramhoz:
def stat(pontszamok) :
    statisztika = [0] * (max(pontszamok) + 1)         # pontszam ami legfeljebb elofordul
    
    for pontszam in pontszamok :
        statisztika[pontszam] += 1
    
    return statisztika
#


# kivalasztasos rendezes az objektum pontszam adattagjat figyelembe veve:
def rendez_pontszam_szerint(eredmeny_lista) :
    for i in range(0, len(eredmeny_lista) - 1) :
        min = eredmeny_lista[i].pontszam
        minindex = i
        for j in range(i + 1, len(eredmeny_lista)) :
            if eredmeny_lista[j].pontszam < min :
                min = eredmeny_lista[j].pontszam
                minindex = j
        if minindex != i :
            tmp = eredmeny_lista[i]
            eredmeny_lista[i] = eredmeny_lista[minindex]
            eredmeny_lista[minindex] = tmp
#

# kivalasztasos rendezes az objektum nev adattagjat figyelembe veve:
def rendez_nev_szerint(eredmeny_lista) :
    for i in range(0, len(eredmeny_lista) - 1) :
        min = eredmeny_lista[i].nev
        minindex = i
        for j in range(i + 1, len(eredmeny_lista)) :
            if eredmeny_lista[j].nev < min :
                min = eredmeny_lista[j].nev
                minindex = j
        if minindex != i :
            tmp = eredmeny_lista[i]
            eredmeny_lista[i] = eredmeny_lista[minindex]
            eredmeny_lista[minindex] = tmp
#

# -----------------------------------------------------------------------------

def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    
    
    
    lista1 = beolvas("./input/zheredmeny.txt")
    lista2 = copy.copy(lista1)                      # shallow copy
    
    assert ((lista1[0] is lista2[0]) == True)       # OK
    
    # ------------------------------------------------------------
    # gyakorlas:
    
    lista3 = copy.deepcopy(lista1)                  # deep copy
    assert ((lista1[0] is lista3[0]) == False)      # OK
    assert ((lista1[0] == lista3[0]) == True)       # OK
    # ------------------------------------------------------------
    
    
    
    
    print(                         elvalaszto_sor                         )
    
    print(lista1[0].pontszam)
    print(lista2[0].pontszam)
    
    print("\nshalow copy: egyik listabol a masikba csak a pointer masolodik\n")
    print("az elson keresztul modositva az objektumot, a masodikon keresztul elerve is modosul:\n")
    lista1[0].pontszam = 27
    print(lista1[0].pontszam)
    print(lista2[0].pontszam)       # shallow copy ellenorzes
    
    
    print(                         elvalaszto_sor                         )
    
    # rendezesek pontszam es nev szerint
    rendez_nev_szerint(lista1)
    rendez_pontszam_szerint(lista2)
    
    print(                         elvalaszto_sor                         )
    print("Nev szerint:\n")
    for eredmeny in lista1 :
        print(eredmeny)
    
    print(                         elvalaszto_sor                         )
    print("Pontszam szerint:\n")
    for eredmeny in lista2 :
        print(eredmeny)
    
    print(                         elvalaszto_sor                         )
    
    
    # ------------------------------------------------------------
    # gyakorlas:
    
    lista0 = copy.copy(lista1)
    
    # rendezes beepitett megoldassal:
    # http://book.pythontips.com/en/latest/lambdas.html
    lista0.sort(key=lambda eredmeny: eredmeny.neptun)
    
    print("rendezes beepitett megoldassal Neptun-kod szerint:\n")
    for eredmeny in lista0 :
        print(eredmeny)
    # ------------------------------------------------------------
    
    
    print(                         elvalaszto_sor                         )
#


# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#












