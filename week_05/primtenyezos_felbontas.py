


print("Melyik szamot?")

melyik_szam = int(input())
print()

# formazashoz:
ideiglenes = melyik_szam
jegyek_szama = 0        # feltetelezve, hogy ertelmes egesz szamot kaptunk inputon
while ideiglenes > 1 :
    ideiglenes /= 10
    jegyek_szama += 1
#
#print("jegyek szama: ", jegyek_szama)


oszto = 2                       # legkisebb primszam

while melyik_szam != 1 :
    if oszto < 0 :
        print("tulcsordulas")
        break
    if melyik_szam % oszto == 0 :
        print("{:>{jegyek_szama}}|{}".format(melyik_szam, oszto,jegyek_szama=jegyek_szama))
        melyik_szam //= oszto
        continue
    else :
        oszto += 1          # a nem primszamokon is vegig lepkedunk,
                            # de ezekkel mar nem lesz oszthato "melyik_szam"
        
#        if oszto % ( 1000000 ) == 0 :   # teszt: pl. 111222333444555666 szamra sokaig futott,
#            print(oszto)                # es igen eppen nem talal primtenyezot 8 jegyuek kozott sem...
#

print("{:>{jegyek_szama}}|".format(1, jegyek_szama=jegyek_szama))
# 




# ugyanez primszamok meghatarozasaval:
"""
# -----------------------------------------------------------------------------
# korabban megoldott feladat:
# https://infopy.eet.bme.hu/lab04/#9
# primszamok 999 helyett a megadott szamig:

import math

prim = [True] * (melyik_szam + 1)    # jelentese: prim[szam] == True ha 'szam' primszam

# prim[0] -> 0      # nem kell, csak az indexeles egyszerusitesehez
# prim[1] -> 1      # nem kell, csak az indexeles egyszerusitesehez

# prim[2] -> 2      # ez mar kell...
# ...
# prim[melyik_szam] -> (melyik_szam+1)


#for szam in range(2, (melyik_szam+1)) : # helyett csak 1000 negyzetgyokeig
for szam in range(2, math.ceil(math.sqrt((melyik_szam+1)))) :
    if prim[szam] :                     # ha a szam nem volt meg kihuzva
        tobbszoros = 2*szam             # a ketszeresetol kezdve
        while tobbszoros < (melyik_szam+1) :       # melyik_szam-ig
            prim[tobbszoros] = False    # kihuzzuk minden
            tobbszoros += szam          # tobbszoroset
        # end while
#

# a megadott szamnal kisebb primszamok listaja:
primszamok = []
for szam in range(2, (melyik_szam+1)) :
    if prim[szam] :
        primszamok.append(szam)
#

# print(primszamok)
# -----------------------------------------------------------------------------

# a primszamok meghatarozasa utan:


# formazashoz:
ideiglenes = melyik_szam
jegyek_szama = 0        # feltetelezve, hogy ertelmes egesz szamot kaptunk inputon
while ideiglenes >1 :
    ideiglenes /= 10
    jegyek_szama += 1
#
#print("jegyek szama: ", jegyek_szama)


i = 0
while melyik_szam != 1 :
    if melyik_szam % primszamok[i] == 0 :
        print("{:>{jegyek_szama}}|{}".format(melyik_szam, primszamok[i],jegyek_szama=jegyek_szama))
        melyik_szam //= primszamok[i]
        continue
    else :
        i += 1
#

print("{:>{jegyek_szama}}|".format(1, jegyek_szama=jegyek_szama))
# https://stackoverflow.com/questions/29044940/how-can-you-use-a-variable-name-inside-a-python-format-specifier/29044976#29044976

"""










