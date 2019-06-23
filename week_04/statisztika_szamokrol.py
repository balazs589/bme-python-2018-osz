
szamok = [0] * 10

print("Irj be egesz szamokat enterrel elvalasztva egymastol! A befejezest ures sor megadasaval jelezd! Ezutan a program megjeleniti az ezek kozul 1 es 10 koze eso ertekek szamat.")


sor = input()
while (sor != "") :
    szam = int(sor)
    if 1 <= szam and szam <= 10 :
        szamok[szam-1] += 1
    print("Add meg a kovetkezo szamot, vagy egy ures sort a befejezeshez!")
    sor = input()
#

print("Az 1 es 10 koze eso szamok eloszlasa:\n")
for index in range(10) :
    print("{:d}:\t".format(index+1), szamok[index], "db")
#
print()


