"""
"""

# -----------------------------------------------------------------------------
# import:


# -----------------------------------------------------------------------------
# fuggvenyek:

def harmas_csoprtositas(szam, hatulrol_hanyadik) :
    if szam == 0 :
        return
    harmas_csoprtositas(szam // 10, hatulrol_hanyadik + 1)
    print(szam % 10, end="")
    if hatulrol_hanyadik % 3 == 0 :
        print(" ", end="")
#

def ezres_szamrendszer(szam) :
    if szam == 0 :
        return
    ezres_szamrendszer(szam // 1000)
    if szam // 1000 == 0 :
        print("{}".format(szam % 1000), end=" ")
    else :
        print("{:03}".format(szam % 1000), end=" ")
#

def beolvas() :
    while True :
        try :
            print("Adj meg egy pozitiv egesz szamot!")
            szam = int(input())
            if szam < 1 :
                continue
            break
        except :
            print("Hibas input!")
        
    return szam
#

def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    szam = beolvas()
    
    # 2 fele megvalositas:
    
    print("\nA megadott szam harmas csoportositassal kiirva:")
    harmas_csoprtositas(szam, 0)
    
    print("\nA megadott szam \"ezres szamrendszerben\" kiirva:")
    ezres_szamrendszer(szam)
    
    print()
    
    print(                         elvalaszto_sor                         )
    
#

# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#

