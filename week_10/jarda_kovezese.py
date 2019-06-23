"""
"""

# -----------------------------------------------------------------------------
# import:


# -----------------------------------------------------------------------------
# fuggvenyek:
def hanyfele_jarda(n) :
    
    if n == 1 :
        return 1
    if n == 2 :
        return 2
    
    return hanyfele_jarda(n - 1) + hanyfele_jarda(n - 2)
    
#

def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    for i in range(1, 10 + 1) :
        print("Ha a jarda hossza {}, akkor {} felekeppen lehet kikovezni.".format(i, hanyfele_jarda(i)))
    
    print(                         elvalaszto_sor                         )
    
#

# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#

