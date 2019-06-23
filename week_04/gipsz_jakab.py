
eredeti = "Gipsz Jakab"

# feltetelezve, hogy a string all egy vezeteknevbol es egy keresztnevbol
# amit 1 db szokoz valaszt el

# keressuk meg hol van a szokoz karakter:

szokoz_helye = 0
megvan = False
while (szokoz_helye < len(eredeti)) and (not megvan) :
    if eredeti[szokoz_helye] == " " :
        megvan = True
    szokoz_helye += 1
# 
# itt lehetne hibat keresni, hogy mi van ha nincs benne szokoz vagy valamelyik szelen van...

forditott = eredeti[szokoz_helye:] + " " + eredeti[:szokoz_helye-1]


print("|" + forditott + "|")