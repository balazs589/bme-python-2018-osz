
# -----------------------------------------------------------------------------
import time
import random
import copy

# -----------------------------------------------------------------------------
# eloadas fuggvenyei:
def buborek(lista):
    for i in range(len(lista)-1, 0, -1):
        for j in range(0, i):
            if lista[j+1] < lista[j]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
#

def kozvetlen(lista):
    for i in range(0, len(lista)-1):
        minidx = i            # minimum keresese
        for j in range(i+1, len(lista)):
            if lista[j] < lista[minidx]:
                minidx = j
        if minidx != i:
            temp = lista[minidx]      # csere
            lista[minidx] = lista[i]
            lista[i] = temp
#

def gyorsrendez(lista, eleje, vege):
    vezer = lista[(eleje + vege) // 2]  # vezerelem: kozepso
    bal = eleje
    jobb = vege
    while bal <= jobb:                  # piros/kek valogatas
        while lista[bal] < vezer:
            bal += 1
        while lista[jobb] > vezer:
            jobb -= 1
        if bal <= jobb:
            tmp = lista[bal]
            lista[bal] = lista[jobb]
            lista[jobb] = tmp
            bal += 1
            jobb -= 1
    
    if eleje < jobb:
        gyorsrendez(lista, eleje, jobb) # rekurzio
    if bal < vege:
        gyorsrendez(lista, bal, vege)
#

# -----------------------------------------------------------------------------
# segedfuggvenyek, hogy azonos parameterekkel lehessen meghivni az osszes algoritmust

def gyors(lista) :
    gyorsrendez(lista, 0, len(lista) - 1)
#

def beepitett(lista) :
    lista.sort()
#


# -----------------------------------------------------------------------------
# rendezes a parameterkent kapott fuggvennyel es idomeres

def kiserlet(algoritmus, lista) :
    
    start = time.time()
    algoritmus(lista)
    stop = time.time()
    
    #print(lista)
    
    return stop - start
#


# -----------------------------------------------------------------------------

def main() :
    
    # print(time.time())
    random.seed(123456789)
    
    N = 10 ** 4
    min = 0
    max = 99
    
    lista = [0] * N
    
    for i in range(len(lista)) :
        lista[i] = random.randrange(min, max + 1)
    
    l1 = copy.copy(lista)
    l2 = copy.copy(lista)
    l3 = copy.copy(lista)
    l4 = copy.copy(lista)
    
                                                             # pl.:
                                                             # 10^4         10^6
                                                                            
    print("{:.10f} sec".format(kiserlet(buborek,    l1)))    # 23.4         
    print("{:.10f} sec".format(kiserlet(kozvetlen,  l2)))    #  9.7         
    print("{:.10f} sec".format(kiserlet(gyors,      l3)))    #  0.06        9.9
    print("{:.10f} sec".format(kiserlet(beepitett,  l4)))    #  0.0099      0.42
    
#


# -----------------------------------------------------------------------------

if __name__ == "__main__" :
    main()
#


