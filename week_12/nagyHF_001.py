
class ElAdatai :
    pass
#


class GrafEl :
    def __init__(self, el_adatai=None) :
        self.el_adatai  = el_adatai
        self.elozo      = None
        self.kovetkezo  = None
    def torol(self) :
        self.elozo.kovetkezo = self.kovetkezo
        self.kovetkezo.elozo = self.elozo
        self.elozo      = None
        self.kovetkezo  = None
        self.el_adatai  = None
#

class ElLista :
    def __init__(self) :
        self.eleje    = GrafEl()      # strazsa1
        self.vege     = GrafEl()      # strazsa2
        
        self.eleje.kovetkezo    = self.vege
        self.vege.elozo         = self.eleje
    
    def hozza_ad(self, el_adatai) :
        
        uj_csomopont = GrafEl(el_adatai)
        
        tmp = self.vege.elozo
        tmp.kovetkezo = uj_csomopont
        
        uj_csomopont.elozo = tmp
        uj_csomopont.kovetkezo = self.vege
        
        self.vege.elozo = uj_csomopont
    
    def keres(self, adat) :
        aktualis = self.eleje.kovetkezo
        while aktualis is not self.vege :
            if aktualis.el_adatai == adat :
                return aktualis
            aktualis = aktualis.kovetkezo
        return None
     
    def torol_elemet(self, adat) :
        elem = self.keres(adat)
        if elem != None :
            elem.torol()
            
    
    def listat_kiurit(self) :
        while self.eleje.kovetkezo is not self.vege :
            self.eleje.kovetkezo.torol()
    
    def megszuntet(self) :
        self.listat_kiurit()
        self.eleje = None
        self.vege = None
        self = None
    
    def kiir_elejetol_vegeig(self) :
        aktualis = self.eleje.kovetkezo
        while aktualis is not self.vege :
            print(aktualis.el_adatai, end=", ")
            aktualis = aktualis.kovetkezo
    
    def kiir_vegetol_elejeig(self) :
        aktualis = self.vege.elozo
        while aktualis is not self.eleje :
            print(aktualis.el_adatai, end=", ")
            aktualis = aktualis.elozo
    
#



class CsomopontAdatai :
    pass
#

class GrafCsomopont :
    def __init__(self, csomopont_adatai=None) :
        # self.sorszam            = None                  # ...
        self.csomopont_adatai   = csomopont_adatai
        self.el_lista = None
        if type(csomopont_adatai) is int :
            self.ellistat_letrehoz()
    
    def ellistat_letrehoz(self) :
        self.el_lista            = ElLista()
        for i in range(1, self.csomopont_adatai) :
            self.el_lista.hozza_ad(i)
    
    def ellistat_torol(self) :
        self.el_lista.megszuntet()
        self.el_lista = None
    
    def torol(self) :
        self.ellistat_torol()
        self.elozo.kovetkezo = self.kovetkezo
        self.kovetkezo.elozo = self.elozo
        self.elozo      = None
        self.kovetkezo  = None
        self.csomopont_adatai  = None
    
    def kiir(self) :
        print("{}.csomopont ellistaja: ".format(self.csomopont_adatai), end="")
        if self.el_lista != None :
            self.el_lista.kiir_elejetol_vegeig()
        else :
            print("Nincs ellista!", end="")
        print()
    
#


class CsomopontLista :
    def __init__(self) :
        self.eleje    = GrafCsomopont()      # strazsa1
        self.vege     = GrafCsomopont()      # strazsa2
        self.eleje.kovetkezo    = self.vege
        self.vege.elozo         = self.eleje
    
    def hozza_ad(self, csomopont_adatai) :
        uj_csomopont = GrafCsomopont(csomopont_adatai)
        
        tmp = self.vege.elozo
        tmp.kovetkezo = uj_csomopont
        
        uj_csomopont.elozo = tmp
        uj_csomopont.kovetkezo = self.vege
        
        self.vege.elozo = uj_csomopont
    
    def kiir_elejetol_vegeig(self) :
        aktualis = self.eleje.kovetkezo
        while aktualis is not self.vege :
            aktualis.kiir()
            aktualis = aktualis.kovetkezo
    
    def kiir_vegetol_elejeig(self) :
        aktualis = self.vege.elozo
        while aktualis is not self.eleje :
            aktualis.kiir()
            aktualis = aktualis.elozo
    
    def keres(self, adat) :
        aktualis = self.eleje.kovetkezo
        while aktualis is not self.vege :
            if aktualis.csomopont_adatai == adat :
                return aktualis
            aktualis = aktualis.kovetkezo
        return None
    
    def torol_csomopontot(self, adat) :
        elem = self.keres(adat)
        if elem != None :
            elem.torol()    # csomopont torlese
            
            # csomopont torlese tobbi csomopont ellistajabol:
            aktualis = self.eleje.kovetkezo
            while aktualis is not self.vege :
                aktualis.el_lista.torol_elemet(adat)
                aktualis = aktualis.kovetkezo
        
        
    def listat_kiurit(self) :
        while self.eleje.kovetkezo is not self.vege :
            self.eleje.kovetkezo.torol()
    
    def megszuntet(self) :
        self.listat_kiurit()
        self.eleje = None
        self.vege = None
    
#




def main() :
    
    print("-" * 79)
    
    el_lista_1 = ElLista()
    
    for i in range(1, 10) :
        el_lista_1.hozza_ad(i)
    
    print("-" * 79)
    el_lista_1.kiir_elejetol_vegeig()
    print()
    
    print("-" * 79)
    el_lista_1.kiir_vegetol_elejeig()
    print()
    
    # -------------------------------------
    print("=" * 79, end="\n\n")
    
    csomopont_lista = CsomopontLista()
    for i in range(1, 10) :
        csomopont_lista.hozza_ad(i)
    
    csomopont_lista.kiir_elejetol_vegeig()
    
    print("=" * 79, end="\n\n")
    csomopont_lista.vege.elozo.el_lista.torol_elemet(5)
    csomopont_lista.kiir_elejetol_vegeig()
    
    print("=" * 79, end="\n\n")
    csomopont_lista.keres(7).el_lista.torol_elemet(3)
    csomopont_lista.kiir_elejetol_vegeig()
    
    print("=" * 79, end="\n\n")
    csomopont_lista.keres(5).el_lista.listat_kiurit()
    csomopont_lista.kiir_elejetol_vegeig()
    
    print("=" * 79, end="\n\n")
    csomopont_lista.torol_csomopontot(6)
    csomopont_lista.kiir_elejetol_vegeig()
    
    print("=" * 79, end="\n\n")
    csomopont_lista.torol_csomopontot(2)
    csomopont_lista.kiir_elejetol_vegeig()
    
    print("=" * 79, end="\n\n")
    csomopont_lista.listat_kiurit()
    csomopont_lista.kiir_elejetol_vegeig()
    
    print("=" * 79, end="\n\n")
    csomopont_lista.megszuntet()
    del csomopont_lista
    
    # csomopont_lista.kiir_elejetol_vegeig()
    
#


import gc
gc.collect()

main()





