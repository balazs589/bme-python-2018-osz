"""

"""

# -----------------------------------------------------------------------------
import re

# -----------------------------------------------------------------------------

class Idopont :
    def __init__(self, ora, perc, masodperc) :
        if ora < 0 or ora > 24 :
            raise ValueError("Hibas ora adat")
        if perc < 0 or perc > 60 :
            raise ValueError("Hibas ora adat")
        if masodperc < 0 or masodperc > 60 :
            raise ValueError("Hibas ora adat")
        self.ora        = ora
        self.perc       = perc
        self.masodperc  = masodperc
    
    def __str__(self) :
        return "ora: {}\tperc: {}\tmasodperc: {}".format(self.ora, self.perc, self.masodperc)
#

def letrehoz_idopontot(group1, group2, group3) :
    
    if group3 == "A" :
        if int(group1) == 12 :
            return Idopont(int(group1) - 12, int(group2), 0)
        else :
            return Idopont(int(group1), int(group2), 0)
    
    elif group3 == "P" :
        if int(group1) == 12 :
            return Idopont(int(group1), int(group2), 0)
        else :
            return Idopont(int(group1) + 12, int(group2), 0)
    
    else :
        return Idopont(int(group1), int(group2), int(group3))
#

def grep() :
    
    idopontok = []
    
    formatum1 = r"^(\d{2}):(\d{2}):(\d{2})$"
    formatum2 = r"^(\d{2})h (\d{2})m (\d{2})s$"
    formatum3 = r"^(\d{2}):(\d{2}) ([AP])M$"
    
    while True :
        print("Adj meg egy idopontot!")
        ido = input()
        if ido == "" :
            break
        
        eredmeny1 = re.search(formatum1, ido)
        eredmeny2 = re.search(formatum2, ido)
        eredmeny3 = re.search(formatum3, ido)
        
        if   eredmeny1 :
            print("Elso formatum")
            try :
                idopontok.append(letrehoz_idopontot(eredmeny1.group(1), eredmeny1.group(2), eredmeny1.group(3)))
            except Exception as e :
                print("Hiba az idopont letrehozasakor.", e)
                
        elif eredmeny2 :
            print("Masodik formatum")
            try :
                idopontok.append(letrehoz_idopontot(eredmeny2.group(1), eredmeny2.group(2), eredmeny2.group(3)))
            except Exception as e :
                print("Hiba az idopont letrehozasakor.", e)
        
        elif eredmeny3 :
            print("Harmadik formatum")
            try :
                idopontok.append(letrehoz_idopontot(eredmeny3.group(1), eredmeny3.group(2), eredmeny3.group(3)))
            except Exception as e :
                print("Hiba az idopont letrehozasakor.", e)
        
        else :
            print("Hibas formatum")
        
    return idopontok
#

# -----------------------------------------------------------------------------

def main() :
    
    idopontok = grep()
    
    for idopont in idopontok :
        print(idopont)
#

# -----------------------------------------------------------------------------
if __name__ == "__main__" :
    main()
#




