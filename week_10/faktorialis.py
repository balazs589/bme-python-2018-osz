
"""
6!  = 6 * 5!
    = 6 * 5 * 4!
    = 6 * 5 * 4 * 3!
    = 6 * 5 * 4 * 3 * 2!
    = 6 * 5 * 4 * 3 * 2 * 1!
    = 6 * 5 * 4 * 3 * 2 * 1 * 0!
    = 6 * 5 * 4 * 3 * 2 * 1 * 1
"""

# -----------------------------------------------------------------------------
# import:



# -----------------------------------------------------------------------------
# fuggvenyek:

def faktorialis(n) :
    """ Fuggveny ami kiszamolja a parameterkent kapott nemnegativ egesz szam faktorialisanak erteket. """
    #if type(n) != int or n < 0 :
    #    raise Exception("A faktorialis fuggveny csak nemnegativ egesz szammal tud szamolni.")
    
    if n == 0 :
        return 1
    else :
        return n * faktorialis(n - 1)
    
#


def main() :
    
    print(faktorialis(6))
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    for i in range(0, 11) :
        print("{}! = {}".format(i, faktorialis(i)))
    
    print(                         elvalaszto_sor                         )
    
    
#

def debughoz() :
    
    """
    Mentes utan a Shell ablak menujeben kattints a Debug / Debugger menupontra. Erre megjelenik egy Debug Control nevu ablak. Ebben pipald be a [ ] Source jelolonegyzetet! Utana a program ablakaban a szokasis Run / Run module menupontra kattints.
    
    A program ilyenkor elindult, de meg egyelore meg van akasztva a legelso sor elott. A Debug Control ablak Over gombjanak nyomkodasaval lehet vegrehajtani a kovetkezo sort. A befejezett ciklustorzsek utan a kiemeneten elkezdenek megjelenni a szamok. A forraskodban latszik, melyik az aktualis sor, a szurke sav mutatja, hol tart epp a vegrehajtas. A Debug Control ablakban pedig (sok jelenleg nem lenyeges informacio mellett) a valtozo erteke figyelheto meg
    """
    
    x = faktorialis(6)
    print(x)
#

# -----------------------------------------------------------------------------
# futtatas:


if __name__ == "__main__" :
    #main()
    debughoz()
#

