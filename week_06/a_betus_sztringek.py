"""
Egy olyan fuggvenyt kell irnod, amely parameterkent sztringek listajat kapja.
Meg kell vizsgalnia a listaban talalhato sztringeket,
es megvalaszolnia ezt a kerdest: van-e olyan sztring, amelyik „a” betuvel kezdodik!
Ennek is legyen logikai tipusu a visszateresi erteke.

"""


# ----------------------------------------------------------------------
def fuggveny(sztring_lista) :
    
    if sztring_lista == [] :
        return False
    for szo in sztring_lista :
        if len(szo) > 0 and szo[0] == "a" :
            return True
    return False
#

# ----------------------------------------------------------------------
def main() :
    #sztring_lista = ["korte", "alma", "barack"]
    #sztring_lista = ["dinnye", "papaja", "", "zeller"]
    sztring_lista = []
    
    print()
    print(sztring_lista)
    
    van_a = fuggveny(sztring_lista)
    
    if van_a :
        print("\nVan \"a\" betuvel kezdodo szo.\n")
    else :
        print("\nNincs \"a\" betuvel kezdodo szo.\n")
#



# =============================================================================

main()