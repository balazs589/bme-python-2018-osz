

import random
import copy                     # https://docs.python.org/3/library/copy.html

lista = list(range(0,5))        # egy darab eredeti lista
                                # a kulonbozo modszereket ezek masolatain lehet kiprobalni

# -----------------------------------------------------------------------------
print("-" * 79)
lista0 = copy.deepcopy(lista)
n=len(lista0)
print(lista0)

# 0. verzio: cserelgetes kezdese az elejerol
for i in range(0,n-1) :
    j = random.randrange(i,n)
    tmp = lista0[i]
    lista0[i] = lista0[j]
    lista0[j] = tmp
    print(lista0)
#


# -----------------------------------------------------------------------------
print("-" * 79)
lista1 = copy.deepcopy(lista)
n=len(lista1)
print(lista1)

# 1. verzio: cserelgetes kezdese a vegerol:
# i -> n-1-i
for i in range(0,n-1) :
    j = random.randrange(0,n-1-i)
    tmp = lista1[n-1-i]
    lista1[n-1-i] = lista1[j]
    lista1[j] = tmp
    print(lista1)
#


# -----------------------------------------------------------------------------

print("-" * 79)
eredeti_lista = copy.deepcopy(lista)
n=len(eredeti_lista)
print(eredeti_lista)
print("-" * 30)

# 2. verzio: uj lista letrehozasaval
uj_lista = []
for i in range(0,n) :
    j = random.randrange(0,n-i)
    veletlen_elem = eredeti_lista.pop(j)
    uj_lista.append(veletlen_elem)
    print(eredeti_lista)
    print(uj_lista)
    print()

# -----------------------------------------------------------------------------
