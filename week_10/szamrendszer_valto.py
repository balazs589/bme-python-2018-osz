"""
"""

# -----------------------------------------------------------------------------
# import:


# -----------------------------------------------------------------------------
# fuggvenyek:

def szamrendszerben_kiir(szam, szamrendszer) :
    if szam == 0 :
        return
    szamrendszerben_kiir(szam // szamrendszer, szamrendszer)
    print(szam % szamrendszer, end="")
    
#

def beolvas() :
    
    while True :
        try :
            print("Add meg az atvaltando pozitiv egesz szamot!")
            szam = int(input())
            if szam < 1 :
                continue
            print("Adj meg egy szamrendszert ( [2, 10] zart intervallumon)!")
            szamrendszer = int(input())
            if szamrendszer < 2 or szamrendszer > 10 :
                continue
            break
        except :
            print("Hibas input!")
        
    return (szam, szamrendszer)
#


def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    (szam, szamrendszer) = beolvas()
    
    print("\nA megadott szam 10 alapu szamrendszerben: {}\n\n{} alapu szamrendszerben: ".format(szam, szamrendszer), end="")
    
    szamrendszerben_kiir(szam, szamrendszer)
    
    print()
    
    print(                         elvalaszto_sor                         )
    
#

# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#

