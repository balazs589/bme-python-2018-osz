

"""
Irj olyan programot, ami ker egy szoveget, es eltavolitja annak elejerol
es vegerol a szokozoket. Ird ki utana idezojelek kozott a vagott sztringet!
"""

print("Irj be egy szoveget!\n")
szoveg = input()

# trimmeles ket lepesben: eloszor szoveg elejerol, majd a vegerol

while (szoveg != "") and (szoveg[0] == " ") :
    szoveg = szoveg[1:]
#

while (szoveg != "") and (szoveg[-1] == " ") :
    szoveg = szoveg[:-1]
#

print("\na megadott szoveg elejerol es vegerol a szokozok levagva:\n")
print('"' + szoveg + '"\n')


