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
    try :
        #f = open(input_file, "rt")
        # https://docs.python.org/3/howto/unicode.html#reading-and-writing-unicode-data
        f = open(input_file, "rt", encoding="utf-8")
        while True :
            sor = f.readline()
            if sor != "" :
                lista.append(sor.rstrip("\n"))
            else :
                break
    except Exception as e :
        print("Hiba:", e)
    finally :
        f.close()
    return lista
#

def k_betu_szures(lista) :
    uj_lista = []
    for szo in lista :
        if szo[0] == "k" :
            uj_lista.append(szo)
    return uj_lista
#

def mentes(output_file, lista) :
    try :
        #f = open(output_file, "wt")
        f = open(output_file, "wt", encoding="utf-8")
        for szo in lista :
            f.write(szo + "\n")
    except Exception as e :
        print("Hiba:", e)
    finally :
        f.close()
#

# -----------------------------------------------------------------------------

def main() :
    
    input_file = "./input/szavak_50.txt"
    lista = betoltes(input_file)
    
    assert (len(lista) == 50)
    for szo in lista :
        print(szo)
    
    lista.sort()
    
    kbetus_lista = k_betu_szures(lista)
    
    mentes("szavak_kbetus.txt", kbetus_lista)
    
    
#


# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#












