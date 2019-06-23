
# "a fuggvenyek ne printeljenek! csak adjak vissza stringkent amit ki kell irni!"



class Datum:
    def __init__(self, ev, honap, nap):
        self.ev = ev
        self.honap = honap
        self.nap = nap
#


class Versenyzo:
    def __init__(self, nev, szuletes, helyezes):
        self.nev = nev
        self.szuletes = szuletes
        self.helyezes = helyezes
#


def datum_kiir(d):
    s = "{}. {}. {}.".format(str(d.ev), str(d.honap), str(d.nap))
    return s
#


def versenyzo_kiir(v):
    s = "{}\t{}\t{}".format(str(v.nev), datum_kiir(v.szuletes), str(v.helyezes))
    return s
#


def main():
    versenyzok = [
        Versenyzo("Am Erika", Datum(1994, 5, 6), 1),
        Versenyzo("Break Elek", Datum(2001, 9, 30), 3),
        Versenyzo("Dil Emma", Datum(1998, 8, 25), 2),
        Versenyzo("Kasza Blanka", Datum(1989, 6, 10), 5),
        Versenyzo("Reset Elek", Datum(2001, 4, 5), 4),
    ];
    
    print()
    print("0-s versenyzo neve:", versenyzok[0].nev)
    print("2-es versenyzo helyezese:", versenyzok[2].helyezes)
    print("4-es versenyzo szuletesi datuma:", datum_kiir(versenyzok[4].szuletes))
    print("1-es versenyzo nevenek kezdobetuje:", versenyzok[1].nev[0])
    
    if versenyzok[1].helyezes <= 3 :
        print("az 1-es versenyzo dobogos: igen")
    else :
        print("az 1-es versenyzo dobogos: nem")
    
    
    if versenyzok[4].helyezes < versenyzok[3].helyezes :
        print("a 4-es versenyzo gyorsabb mint a 3-as versenyzo: igen")
    else :
        print("a 4-es versenyzo gyorsabb mint a 3-as versenyzo: nem")
    
    if versenyzok[1].szuletes.ev == versenyzok[2].szuletes.ev :
        print("az 1-es versenyzo ugyanabban az evben szuletett, mint a 2-es: igen")
    else :
        print("az 1-es versenyzo ugyanabban az evben szuletett, mint a 2-es: nem")
    
    print()
    print("az 1-es versenyzo adatai:")
    print(versenyzo_kiir(versenyzok[1]))
    
    
    
    print("-" * 79)
    print("a versenyzok listaja:")
    
    
    for i in range(len(versenyzok)) :
        print(versenyzo_kiir(versenyzok[i]))
    
    
    print()
    
#



# 0-s versenyzo neve
# 2-es versenyzo helyezese
# 4-es versenyzo szuletesi datuma (ird meg a datum_kiir fuggvenyt!)
# 1-es versenyzo nevenek kezdobetuje
# az 1-es versenyzo dobogos-e? igen/nem
# az 4-es versenyzo gyorsabb-e, mint a 3-as versenyzo?
# az 1-es versenyzo ugyanabban az evben szuletett-e, mint a 2-es?
# egeszitsd ki a versenyzo_kiir() fuggvenyt, es ird ki az 1-es versenyzo adatait
# vegul listazd ki az osszes versenyzot sorszamozva, osszes adatukkal.

main()








