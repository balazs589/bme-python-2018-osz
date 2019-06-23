
"""
"""

# -----------------------------------------------------------------------------
# import:
import turtle
import fraktal

# -----------------------------------------------------------------------------
# fuggvenyek:

def hopehely_hogy_kozepen_legyen(teljes_meret) :
    turtle.up()
    turtle.backward(teljes_meret / 4)
    turtle.left(60)
    turtle.backward(teljes_meret / 2)
    turtle.down()
    turtle.width(2)
#

def hopehely(hossz, bonyolultsag) :
    for _ in range(3) :
        fraktal.rekurziv(hossz, bonyolultsag)
        turtle.right(120)
#


def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    teljes_meret = 500.0
    turtle.delay(0.9)
    
    
    for i in range(5) :
        #turtle.up()
        #turtle.setheading(0)
        #turtle.setpos(0, 0)
        turtle.reset()
        
        hopehely_hogy_kozepen_legyen(teljes_meret)
        hopehely(teljes_meret, i)
    
    turtle.mainloop()
    
    print(                         elvalaszto_sor                         )
    
#

# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#

