
# https://infopy.eet.bme.hu/lab03/#6
# ...

szamok = [2.5, -69, 5.4, -8, -7.7, 6, 2.9, -10, -3, 9.8]
negativ = []

print("\nOsszesen 10 szam van.")
for index in range(len(szamok)) :
    print("[{:d}] =".format(index), szamok[index])
    if szamok[index] < 0 :
        negativ.append(index)
#

print()
print("Ebbol {:d} szam negativ.".format(len(negativ)))
print("Indexeik: ", end="")
for index in negativ :
    print(index, end=" ")
print()
#


print("\nEzek pedig a kovetkezo szamok:")

for i in range(len(negativ)) :
    print("{:d}. [{:d}] = {}".format(i+1, negativ[i], szamok[negativ[i]]))
#

print()

# ------------------------------------------------------------------


