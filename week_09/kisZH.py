


def beolvas() :
    szamok = []
    while True :
        try :
            szamok.append(float(input()))
        except Exception as e :
            break
    return szamok
#

def van_e_kisebb(lista, szam) :
    for elem in lista :
        if elem < szam :
            return True
    return False
#

def main() :
    
    
    lista = beolvas()
    
    if van_e_kisebb(lista, 5) :
        print("VOLT")
    else :
        print("NEM VOLT")
    
#


main()



