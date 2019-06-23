
#szoveg = "abcdefghijklmnopqrstuvwxyz"
print("kodolando szoveg:")
szoveg = input()

print("kodolo karakter (angol abc kisbetui kozul 1 db):")
kodolo_karakter = input()   # hibakezeles nincs megvalositva

kodszam = ord(kodolo_karakter) - ord("a")
abc_hossz = ord("z") - ord("a") + 1     # igy nincs magikus 26-os
elso = ord("a")

print("----------------------------------------------------")
print("szoveg a kodolas utan:")
for c in szoveg :
    if ord("a") <= ord(c) and ord(c) <= ord("z") :
        print(chr(((ord(c) - elso) + kodszam ) % abc_hossz + elso), end="" )
    else :
        print(c, end="" )
#
print()
