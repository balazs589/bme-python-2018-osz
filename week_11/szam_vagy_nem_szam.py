"""

"""

# -----------------------------------------------------------------------------
# import:

# -----------------------------------------------------------------------------
# osztalyok :

# -----------------------------------------------------------------------------
# fuggvenyek:

def szam_e(szoveg) :
    try :
        szam = int(szoveg)
        return True
    except :
        return False
#

# -----------------------------------------------------------------------------

def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    
    assert (szam_e("123")       == True)
    assert (szam_e("almafa")    == False)
    assert (szam_e("3.14")      == False)
    
    
    print(                         elvalaszto_sor                         )
    
#


# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#












