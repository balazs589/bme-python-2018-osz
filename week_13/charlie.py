
def kiszolgal(fagyik) :
    
    while True :
        rendeles = input()
        if rendeles == "" :
            break
        
        if rendeles not in fagyik :
            print(rendeles + " nem is volt!")
        elif fagyik[rendeles] == 0 :
            print(rendeles + " kifogyott!")
        else :
            print("kosz, ocsi!")
            fagyik[rendeles] -= 1
    
#

def main() :
    
    fagyik =    {
                    "pisztacia"     : 0,
                    "vanilia"       : 3,
                    "tutti-frutti"  : 8,
                    "karamell"      : 4,
                    "rumos dio"     : 5,
                    "kave"          : 9,
                }
    
    kiszolgal(fagyik)
#



if __name__ == "__main__" :
    main()
#