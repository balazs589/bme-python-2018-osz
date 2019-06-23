
def rendezett_e(lista) :
    """
    Fuggveny ami eldonti, hogy a parameterkent kapott listaban
    novekvo sorrendben szerepelnek-e az elemek.
    
    Kis-nagybetukre mukodik ekezetesekre nem.
    """
    
    if type(lista[0]) is str :
        for i in range(1,len(lista)) :
            #if lista[i - 1] > lista[i] :   # kis - nagy betukre:
            if lista[i - 1].upper() > lista[i].upper() :
                return False
    else :
        for i in range(1,len(lista)) :
            if lista[i - 1] > lista[i] :
                return False
    return True
    
#


def main() :
    
    lista1 = [10, 28, 30, 41, 57, 68, 72, 81, 97]
    lista2 = ["alma", "barack", "cekla", "zeller", "dinnye", "egres", "fuge"]
    
    lista3 = ["alma", "barack", "cekla", "dinnye", "egres", "fuge"]
    lista4 = ["alma", "barack", "Cekla", "dinnye", "egres", "fuge"]
    lista5 = ["alma", "barack", "cekla", "dinnye", "egres", "fuge"]
    
    
    print(rendezett_e(lista1))
    print(rendezett_e(lista2))
    print(rendezett_e(lista3))
    print(rendezett_e(lista4))
    print(rendezett_e(lista5))
#


# https://stackoverflow.com/questions/6523791/why-is-python-running-my-module-when-i-import-it-and-how-do-i-stop-it/6523852#6523852
if __name__ == "__main__" :
    main()
#


