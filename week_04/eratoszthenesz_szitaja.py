import math

prim = [True] * 1000    # jelentese: prim[szam] == True ha 'szam' primszam

# prim[0] -> 0      # nem kell, csak az indexeles egyszerusitesehez
# prim[1] -> 1      # nem kell, csak az indexeles egyszerusitesehez

# prim[2] -> 2      # ez mar kell...
# ...
# prim[999] -> 999


#for szam in range(2, 1000) : # helyett csak 1000 negyzetgyokeig
for szam in range(2, math.ceil(math.sqrt(1000))) :
    if prim[szam] :                     # ha a szam nem volt meg kihuzva
        tobbszoros = 2*szam             # a ketszeresetol kezdve
        while tobbszoros < 1000 :       # 999-ig
            prim[tobbszoros] = False    # kihuzzuk minden
            tobbszoros += szam          # tobbszoroset
        # end while
#


x = 0
# es kiirjuk ami nem lett kihuzva:
print("A 999-nel kisebb primszamok listaja:")
for szam in range(2, 1000) :
    if prim[szam] :
        x += 1
        print(szam)
#
