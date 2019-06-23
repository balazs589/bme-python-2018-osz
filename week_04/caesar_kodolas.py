
#szoveg = "abcdefghijklmnopqrstuvwxyz"
print("irj be egy szot ami csak az angol abc kisbetuibol all")
szoveg = input()


for c in szoveg :
    if ord("a") <= ord(c) and ord(c) <= ord("z") :
        if c != "z":
            print(chr(ord(c)+1), end="")
        else :
            print(chr( ord(c) - ( ord("z") - ord("a") ) ), end="" )
    else :
        print(c, end="" )
#
print()





