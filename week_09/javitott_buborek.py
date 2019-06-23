import random
import copy

from rendezett_e import rendezett_e
from rendezesek_hatekonysaga import kiserlet

# -----------------------------------------------------------------------------

def buborek(lista):
    for i in range(len(lista)-1, 0, -1):
        for j in range(0, i):
            if lista[j+1] < lista[j]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
#

def javitott_buborek(lista):
    for i in range(len(lista)-1, 0, -1):
        
        volt_csere = False
        
        for j in range(0, i):
            if lista[j+1] < lista[j]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
                volt_csere = True
        
        # javitott verzioban ha a lista eleje rendezett mar nem kell tovabb rendezni:
        if not volt_csere :
            break
#



# -----------------------------------------------------------------------------

def main() :
    
    
    
    # -------------------------------------------------------------------------
    # veletlen lista elkeszitese :
    
    #random.seed(123456789)
    
    N = 10 ** 3
    min = 0
    max = 99
    
    lista = [0] * N
    
    for i in range(len(lista)) :
        lista[i] = random.randrange(min, max + 1)
    
    l5 = copy.copy(lista)       # l5 a rendezendo lista
    # -------------------------------------------------------------------------
    
    #print(l5)
    
    # javitott verzionak akkor van jelentosege, ha a lista vegeben nincsenek kis elemek
    # pl. ha a lista eleve rendezett, akkor az eredeti buborekrendezessel ellentetben
    # a javitott verzio szinte azonnal kesz van
    
    #l5.sort()
    #print("{:.10f} sec".format(kiserlet(buborek,          l5)))
    print("{:.10f} sec".format(kiserlet(javitott_buborek, l5)))
    
    #print(l5)
    
    # ellenorzes:
    if rendezett_e(l5) :
        print("\nA lista rendezett.")
    else :
        print("\nA lista NEM rendezett.")
        
    
#

# -----------------------------------------------------------------------------

main()

