

# -----------------------------------------------------------------------------



def hash_fuggveny(szo):
    if ord(szo[0]) < ord("a") or ord(szo[0]) > ord("z") :
        raise ValueError("A kapott sztring ( '{}' ) alkalmatlan a hasheleshez: nem az „a...z” karakterek valamelyikevel kezdodik!".format(szo))
    return ord(szo[0]) - ord("a")
#

def hash_tabla_letrehoz() :
    elemek_szama = ord("z") - ord("a") + 1
    hash_tabla = []
    for _ in range(elemek_szama) :
        hash_tabla.append([])
    return hash_tabla
#


def hash_tabla_betesz(tabla, szo) :
    index = hash_fuggveny(szo)
    if szo not in tabla[index] :
        tabla[index].append(szo)
#


def hash_tabla_debug(tabla) :
    for i in range(len(tabla)) :
        print("{}: {}".format(chr(ord("a") + i), tabla[i]))
#


def hash_tabla_benne_van(tabla, szo) :
    index = hash_fuggveny(szo)
    if szo in tabla[index] :
        return True
    else :
        return False
#

def hash_tabla_kivesz(tabla, szo) :
    index = hash_fuggveny(szo)
    if szo in tabla[index] :
        tabla[index].remove(szo)
#


def hash_tabla_listaz(tabla) :
    for i in range(len(tabla)) :
        for szo in tabla[i] :
            print(szo, end=", ")
#


# -----------------------------------------------------------------------------

def main() :
    
    print("-" * 79)
    
    szavak1 = ["alma", "korte", "barack"]
    szavak2 = ["alma", "ananasz", "avokado"]
    szavak = szavak1 + szavak2
    
    hash_tabla = hash_tabla_letrehoz()
    
    for szo in szavak :
        hash_tabla_betesz(hash_tabla, szo)
        #print(hash_fuggveny(szo))
    
    hash_tabla_betesz(hash_tabla, "zebra")
    try :
        hash_tabla_betesz(hash_tabla, "Zebra")
    except ValueError as verr :
        print("Hiba: {}".format(verr))
    
    print()
    print("-" * 79)
    hash_tabla_debug(hash_tabla)
    
    print()
    print("-" * 79)
    print(hash_tabla_benne_van(hash_tabla, "avokado"))
    print(hash_tabla_benne_van(hash_tabla, "avokad"))
    
    print()
    print("-" * 79)
    hash_tabla_listaz(hash_tabla)
    
    
    print()
    print("-" * 79)
    hash_tabla_debug(hash_tabla)
    print()
    print("-" * 79)
    hash_tabla_kivesz(hash_tabla, "korte")
    hash_tabla_kivesz(hash_tabla, "koret")
    hash_tabla_debug(hash_tabla)
    
    
    print()
    print("-" * 79)
    hash_tabla_listaz(hash_tabla)
        
#

# -----------------------------------------------------------------------------

if __name__ == "__main__" :
    main()
#

