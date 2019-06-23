
def letrehoz(input_file) :
    
    eredmenyek = dict()
    
    with open(input_file, "rt", encoding="utf-8") as f :
        while True :
            sor = f.readline()
            if sor != "" :
                eredmeny = sor.split(":")
                eredmenyek[eredmeny[0]] = int(eredmeny[1])
            else :
                break
    
    return eredmenyek
#

def szotart_kiir(eredmenyek) :
    for neptun, pontszam in eredmenyek.items() :
        print(neptun, ":", pontszam)
#

def stat(eredmenyek) :
    statisztika = dict()
    for pontszam in eredmenyek.values() :
        if pontszam not in statisztika :
            statisztika[pontszam] = 1
        else :
            statisztika[pontszam] += 1
    
    return statisztika
    
#


def stat_neptun(eredmenyek) :
    
    kiknek = dict()
    for neptun, pontszam in eredmenyek.items() :
        if pontszam not in kiknek :
            kiknek[pontszam] = [neptun]
        else :
            kiknek[pontszam].append(neptun)
    
    return kiknek
    
#


def szotart_rendezve_kiir(d) :
    for key in sorted(d.keys()) :
        print("{}:\t{}".format(key, d[key]))
#

def main() :
    
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    eredmenyek = letrehoz("./zheredmeny.txt")
    
    print(                         elvalaszto_sor                         )
    szotart_kiir(eredmenyek)
    
    print(                         elvalaszto_sor                         )
    print("A ZH-t {} hallgato irta meg.".format(len(eredmenyek)))
    
    print(                         elvalaszto_sor                         )
    szotart_rendezve_kiir(stat(eredmenyek))
    
    print(                         elvalaszto_sor                         )
    szotart_rendezve_kiir(stat_neptun(eredmenyek))
    
    print(                         elvalaszto_sor                         )
    
    
    
    
#



if __name__ == "__main__" :
    main()
#



# ----------------------------------------------------------------------------
# minta megoldas honlaprol:

def beolvas(fajlnev):
    d = {}
    with open(fajlnev, "rt") as f:
        for s in f:
            neptun, pont = s.split(":")
            d[neptun] = int(pont)
    return d


def hisztogram(d):
    """Pontszamok szerinti hisztogram."""
    # Az eredeti szotar ertekei a pontszamok.
    # Beszuraskor lehet epp uj elem jon letre:
    # ezt itt a .get() fuggvennyel oldjuk meg.
    # Az if pont in p esetszetvalasztas is jo lenne.
    p = {}
    for pont in d:
        p[pont] = p.get(pont, 0) + 1
    return p


def kiknek(d):
    """Pontszamok szerinti NEPTUN kod listak."""
    # Itt latni kell a pontokat es a NEPTUN kodokat
    # is, ugyhogy d.items()-en iteral a ciklus.
    # Ha az adott pontszamot meg nem lattuk,
    # uj listat kell letrehozni.
    n = {}
    for neptun, pont in d.items():
        if pont not in n:
            n[pont] = []
        n[pont].append(neptun)
    return n


def print_dict(d):
    """Kulcsok szerint novekvo sorban listaz."""
    for key, val in sorted(d.items()):
        print("{}: {}".format(key, val))


def main2():
    d = beolvas("zheredmeny.txt")   # { neptun: pont }
    print("Letszam:", len(d))
    h = hisztogram(d)               # { pont: letszam }
    print_dict(h)
    n = kiknek(d)                   # { pont: [neptun, neptun, ...] }
    print_dict(n)
