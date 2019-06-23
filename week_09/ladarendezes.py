import random
import copy

from rendezett_e import rendezett_e
from rendezesek_hatekonysaga import kiserlet

# -----------------------------------------------------------------------------



def ladarendezes_100_ertekre(lista):
    
    max = 99
    T = [0] * (max + 1)
    
    for szam in lista :
        T[szam] += 1
    
    j = 0
    for i in range(len(T)) :
        while T[i] > 0 :
            lista[j] = i
            j += 1
            T[i] -= 1
    
#




# -----------------------------------------------------------------------------

def main() :
    
    
    
    # -------------------------------------------------------------------------
    # veletlen lista elkeszitese :
    
    #random.seed(123456789)
    
    N = 10 ** 5
    min = 0
    max = 99
    
    lista = [0] * N
    
    for i in range(len(lista)) :
        lista[i] = random.randrange(min, max + 1)
    
    l6 = copy.copy(lista)       # l6 a rendezendo lista
    # -------------------------------------------------------------------------
    
    #print(l6)
    
    # javitott verzionak akkor van jelentosege, ha a lista vegeben nincsenek kis elemek
    # pl. ha a lista eleve rendezett, akkor az eredeti buborekrendezessel ellentetben
    # a javitott verzio szinte azonnal kesz van
    
    #l6.sort()
    print("{:.10f} sec".format(kiserlet(ladarendezes_100_ertekre, l6)))
    
    #print(l6)
    
    # ellenorzes:
    if rendezett_e(l6) :
        print("\nA lista rendezett.")
    else :
        print("\nA lista NEM rendezett.")
        
    
#

# -----------------------------------------------------------------------------

main()

