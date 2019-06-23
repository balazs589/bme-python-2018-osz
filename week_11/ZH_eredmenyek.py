"""

"""

# -----------------------------------------------------------------------------
# import:

# -----------------------------------------------------------------------------
# osztalyok :

# -----------------------------------------------------------------------------
# fuggvenyek:

def beolvas(input_file) :
    szamok = []
    
    with open(input_file, "rt", encoding="utf-8") as f :
        while True :
            sor = f.readline()
            if sor != "" :
                szamok.append(int(sor))
            else :
                break
    
    return szamok
#

def stat(pontszamok) :
    statisztika = [0] * 11          # pontszamok [0, 10] zart intervallumon
    
    for pontszam in pontszamok :
        statisztika[pontszam] += 1
    
    return statisztika
#

def stat_kiir(statisztika) :
    sikeres = 0
    
    for pontszam in range(len(statisztika)) :
        letszam = statisztika[pontszam]
        print("{:>3} db {:>2} pontos".format(letszam, pontszam))
        if pontszam >= 4 :
            sikeres += letszam
    
    print("Atment: {} fo, {:.2f}%".format(sikeres, 100.0 * sikeres / sum(statisztika)))
    
#


# -----------------------------------------------------------------------------

def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    
    stat_kiir(stat(beolvas("./input/kzh_pontszam.txt")))
    
    
    print(                         elvalaszto_sor                         )
    
#


# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#












