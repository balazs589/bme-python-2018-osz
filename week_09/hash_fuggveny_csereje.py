# hash_tabla.py + automatikus_tesztek.py fuggvenyei atmasolva es modositva
# hash_fuggveny helyett uj_hash_fuggveny
# tabla merete megadhato

# -----------------------------------------------------------------------------

TABLA_MERET = 20

def uj_hash_fuggveny(szo, tabla_meret):
    return hash(szo) % tabla_meret
#

def hash_tabla_letrehoz(tabla_meret) :
    hash_tabla = []
    for _ in range(tabla_meret) :
        hash_tabla.append([])
    return hash_tabla
#

def hash_tabla_betesz(tabla, szo) :
    index = uj_hash_fuggveny(szo, len(tabla))
    if szo not in tabla[index] :
        tabla[index].append(szo)
#

def hash_tabla_debug(tabla) :
    for i in range(len(tabla)) :
        print("{}:\t{}".format(i, tabla[i]))
#

def hash_tabla_benne_van(tabla, szo) :
    index = uj_hash_fuggveny(szo, len(tabla))
    if szo in tabla[index] :
        return True
    else :
        return False
#

def hash_tabla_kivesz(tabla, szo) :
    index = uj_hash_fuggveny(szo, len(tabla))
    if szo in tabla[index] :
        tabla[index].remove(szo)
#

def hash_tabla_listaz(tabla) :
    for i in range(len(tabla)) :
        for szo in tabla[i] :
            print(szo, end=", ")
#


# -----------------------------------------------------------------------------

def teszt2() :
    
    tabla = hash_tabla_letrehoz(TABLA_MERET)
    assert (type(tabla) is list)
    assert (len(tabla) == TABLA_MERET)
    
    return tabla
#

def teszt3(tabla) :
    
    hash_tabla_betesz(tabla, "alma")
    hash_tabla_betesz(tabla, "barack")
    hash_tabla_betesz(tabla, "alma")
    hash_tabla_betesz(tabla, "avokado")
    hash_tabla_betesz(tabla, "korte")
    assert (hash_tabla_benne_van(tabla, "alma")       == True)
    assert (hash_tabla_benne_van(tabla, "barack")     == True)
    assert (hash_tabla_benne_van(tabla, "avokado")    == True)
    
#

def teszt4(tabla) :
    
    hash_tabla_kivesz(tabla, "alma")
    hash_tabla_kivesz(tabla, "avokado")
    assert (hash_tabla_benne_van(tabla, "alma")       == False)
    assert (hash_tabla_benne_van(tabla, "avokado")    == False)
    
#

# -----------------------------------------------------------------------------
def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    
    print(                         elvalaszto_sor                         )
    # hash teszt:
    print(hash("alma"))
    print(hash("barack"))
    print(hash("dinnye"))
    
    print(                         elvalaszto_sor                         )
    # negativ modulo teszt:
    for i in range(-9, 20) :
        print(i % 10)
    
    print(                         elvalaszto_sor                         )
    tabla = teszt2()
    
    print(                         elvalaszto_sor                         )
    teszt3(tabla)
    
    print(                         elvalaszto_sor                         )
    teszt4(tabla)
    
    print(                         elvalaszto_sor                         )
    
    for c in "abcdefghijklmnopqrstuvwxyz" :
        hash_tabla_betesz(tabla, c)
    hash_tabla_debug(tabla)
    
    print(                         elvalaszto_sor                         )
    
    for c in "abcdefghijklmnopqrstuvwxyz" :
        hash_tabla_kivesz(tabla, c)
    hash_tabla_debug(tabla)
    
    print(                         elvalaszto_sor                         )    
#

# -----------------------------------------------------------------------------

if __name__ == "__main__" :
    main()
    
#

