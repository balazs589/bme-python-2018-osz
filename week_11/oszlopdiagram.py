"""

"""

# -----------------------------------------------------------------------------
# import:
import turtle           as t
import ZH_eredmenyek    as zh
import dolgozatok       as dolgozzatok

# -----------------------------------------------------------------------------
# osztalyok :


# -----------------------------------------------------------------------------
# fuggvenyek:

# oszlopdiagramhoz:
def oszlop(alap, magas) :
    t.down()
    t.begin_fill()
    
    t.forward(alap)
    t.left(90)
    t.forward(magas)
    t.left(90)
    t.forward(alap)
    t.left(90)
    t.forward(magas)
    t.left(90)
    
    t.end_fill()
    
    t.up()
#

def ugras_kovetezore(hossz) :
    t.up()
    t.forward(hossz)
#

# oszlopdiagram rajzolasa:
def grafikon(width, height, statisztika) :
    
    t.color("black", "white")       #
    oszlop(width, height)           # keret
    t.color("black", "black")       # 
    
    # hogy a grafikon nagyjabol ki legyen toltve:
    fel_oszlop_meret = width / (len(statisztika) + 1.5) / 3.0
    legmagasabb_oszlop = float(max(statisztika))
    
    # oszlopok:
    for i in range(len(statisztika)) :
        ugras_kovetezore(3 * fel_oszlop_meret)
        oszlop(2 * fel_oszlop_meret, 0.8 * height * float(statisztika[i]) / legmagasabb_oszlop)
    
    # mozgas vissza origohoz:
    t.up()
    t.backward(len(statisztika) * 3 * fel_oszlop_meret)
#


def turtle_kezdes(screen_width, screen_height) :
    
    t.setup (screen_width, screen_height, startx=0, starty=0)
    
    bal_oldal   = 0.0
    jobb_oldal  = screen_width
    alja        = 0.0
    teteje      = screen_height
    
    t.mode("world")
    t.setworldcoordinates(bal_oldal, alja, jobb_oldal, teteje)
    
    t.tracer(0)
    t.hideturtle()
    t.color("black", "black")
    t.up()
    
#

# -----------------------------------------------------------------------------

def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    # kis ZH feladat statisztikaja:
    kisZH_stat = zh.stat(zh.beolvas("./input/kzh_pontszam.txt"))
    
    # "NEPTUN kodos feladat" eredmenylistaja:
    eredmeny_lista = dolgozzatok.beolvas("./input/zheredmeny.txt")
    
    # ebbol kibanyaszva a pontszamok listaja:
    # https://stackoverflow.com/questions/2739800/extract-list-of-attributes-from-list-of-objects-in-python
    # https://www.python.org/dev/peps/pep-0289/
    pontszamok = [eredmeny.pontszam  for eredmeny in eredmeny_lista]
    # es a beloluk keszitett statisztika:
    dolgozatok_stat = dolgozzatok.stat(pontszamok)
    
    
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~ rajzolgatas: ~~~~~~~~~~~~~~~~~~~~~~~~~
    screen_width    = 800
    screen_height   = 550
    oldal_keret     = 50.0
    alul_keret      = 50.0
    
    turtle_kezdes(screen_width, screen_height)
    
    grafikon_width      = screen_width - 2.0 * oldal_keret
    grafikon_height     = (screen_height - 3.0 * alul_keret) / 2.0
    
    # egyik es masik feladat oszlopdiagramjai:
    
    t.goto(oldal_keret, alul_keret)
    grafikon(grafikon_width, grafikon_height, kisZH_stat)           # alul
    
    t.goto(oldal_keret, 2 * alul_keret + grafikon_height)
    grafikon(grafikon_width, grafikon_height, dolgozatok_stat)      # felul
    
    t.mainloop()
    
    
    print(                         elvalaszto_sor                         )
#


# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#












