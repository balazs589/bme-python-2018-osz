"""

"""

# -----------------------------------------------------------------------------
# import:

# -----------------------------------------------------------------------------
# osztalyok :

# -----------------------------------------------------------------------------
# fuggvenyek:

def betoltes(input_file) :
    lista = []
    with open(input_file, "rt", encoding="utf-8") as f :
        while True :
            sor = f.readline()
            if sor != "" :
                lista.append(sor.rstrip("\n"))
            else :
                break
    return lista
#

def elso_kozos_elemet_keres(input_fajl1, input_fajl2) :
    lista1 = betoltes(input_fajl1)
    lista2 = betoltes(input_fajl2)
    
    kozos_elem = None
    
    for elem in lista1 :
        if elem in lista2 :
            return elem
    
    return None
    
#

# -----------------------------------------------------------------------------

def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    metrovonalak = [    "m1",
                        "m2",
                        "m3",
                        "m4"]
    
    for i in range(0, len(metrovonalak)) :
        for j in range(i + 1, len(metrovonalak)) :
            
            print()
            egyik = "./input/" + metrovonalak[i] + ".txt"
            masik = "./input/" + metrovonalak[j] + ".txt"
            kozos_allomas = elso_kozos_elemet_keres(egyik, masik)
            
            if kozos_allomas != None :
                print(metrovonalak[i], "es", metrovonalak[j], "kozott atszallasi lehetoseg:\n", kozos_allomas)
            else:
                print(metrovonalak[i], "es", metrovonalak[j], "kozott NINCS atszallasi lehetoseg\n")
    
    print(                         elvalaszto_sor                         )
    
#


# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#












