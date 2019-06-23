
"""
Kozismert magyar nyelvu palindrom mondat az „Indul a gorog aludni.”

Akkor is palindrom mondatnak tekintunk egy mondatot, ha megforditva mashova kell
rakni a szokozoket, hogy onmagat visszakapjuk. Ezert a szokozok eltavolitasa utan
kell megvizsgalni, hogy a kapott karakterlanc oda-vissza olvasva megegyezik onmagaval.

(   + kisbetu nagybetuk sem szamitanak
    + illetve meg az irasjeleket is ki kellene szurni...)

"""

szoveg = "Indul a gorog aludni."


# elozo feladatbol:

szoveg_szokozok_nelkul = ""
for c in szoveg :
    if  (       (c != " ")
            and (c != ".")
            and (c != ",")
            and (c != "?")
            and (c != "!")
            and (c != ":")
            and (c != ";") ) :
        szoveg_szokozok_nelkul += c.lower()
#
# print(szoveg_szokozok_nelkul)


palindrom = True
index = 0
while (index < len(szoveg_szokozok_nelkul)) and (palindrom) :
    if szoveg_szokozok_nelkul[index] != szoveg_szokozok_nelkul[-(index+1)] :
        palindrom = False
    index += 1
#

print("A vizsgalt mondat:")
print(szoveg)

if palindrom :
    print("Ez egy palindrom mondat.")
else :
    print("Ez nem palindrom mondat.")
#





