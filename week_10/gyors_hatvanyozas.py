"""
"A hatvanyozas elvegezheto annal gyorsabban is, mintha a kitevonek megfelelo szamu szorzast csinalnank. Pl. a8 = a4·a4, a4 = a2·a2 es a2 = a·a miatt a nyolcadikra hatvanyozashoz mindossze harom szorzasra van szukseg."
"""
# -----------------------------------------------------------------------------
# import:


# -----------------------------------------------------------------------------
# fuggvenyek:

def gyors_hatvanyozas(a, k) :
    
    if k == 0 :
        return 1
    elif k % 2 == 1 :
        return a * gyors_hatvanyozas(a, k - 1)
    else :
        return gyors_hatvanyozas(a, k // 2) * gyors_hatvanyozas(a, k // 2)
#


def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    for i in range(1, 16 + 1) :
        print("2^{}\t= {}".format(i, gyors_hatvanyozas(2, i)))
    
    print(                         elvalaszto_sor                         )
    
    
#

# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#

