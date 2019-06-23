


# -----------------------------------------------------------------------------
import hash_tabla as h

# -----------------------------------------------------------------------------

def teszt1() :
    
    assert (h.hash_fuggveny("a") == 0)
    assert (h.hash_fuggveny("z") == 25)
    
#

def teszt2() :
    
    tabla = h.hash_tabla_letrehoz()
    assert (type(tabla) is list)
    assert (len(tabla) == 26)
    
    return tabla
#

def teszt3(tabla) :
    
    h.hash_tabla_betesz(tabla, "alma")
    h.hash_tabla_betesz(tabla, "barack")
    h.hash_tabla_betesz(tabla, "alma")
    h.hash_tabla_betesz(tabla, "avokado")
    h.hash_tabla_betesz(tabla, "korte")
    assert (h.hash_tabla_benne_van(tabla, "alma")       == True)
    assert (h.hash_tabla_benne_van(tabla, "barack")     == True)
    assert (h.hash_tabla_benne_van(tabla, "avokado")    == True)
    
#

def teszt4(tabla) :
    
    h.hash_tabla_kivesz(tabla, "alma")
    h.hash_tabla_kivesz(tabla, "avokado")
    assert (h.hash_tabla_benne_van(tabla, "alma")       == False)
    assert (h.hash_tabla_benne_van(tabla, "avokado")    == False)
    
#


def main():
    
    # assert True           # -> fut tovabb
    # assert False          # -> AssertionError
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    
    print(                         elvalaszto_sor                         )
    teszt1()
    
    print(                         elvalaszto_sor                         )
    tabla = teszt2()
    
    print(                         elvalaszto_sor                         )
    teszt3(tabla)
    
    print(                         elvalaszto_sor                         )
    teszt4(tabla)
    
    print(                         elvalaszto_sor                         )
    
    for c in "abcdefghijklmnopqrstuvwxyz" :
        h.hash_tabla_betesz(tabla, c)
    h.hash_tabla_debug(tabla)
    
    print(                         elvalaszto_sor                         )
    
    for c in "abcdefghijklmnopqrstuvwxyz" :
        h.hash_tabla_kivesz(tabla, c)
    h.hash_tabla_debug(tabla)
    
    print(                         elvalaszto_sor                         )
    
    
#


# -----------------------------------------------------------------------------


if __name__ == "__main__" :
    main()
#


# -----------------------------------------------------------------------------

"""
# https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python/5142453#5142453

assert condition =>
                            if not condition:
                                raise AssertionError()
#


# https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python/5143044#5143044

assert condition =>
                            if __debug__:
                                if not condition:
                                    raise AssertionError
#


debug mod kikapcsolasa:
python -O automatikus_tesztek.py
"""