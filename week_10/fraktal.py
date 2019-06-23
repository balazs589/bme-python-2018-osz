"""
"""

# -----------------------------------------------------------------------------
# import:
import turtle

# -----------------------------------------------------------------------------
# fuggvenyek:

def szakasz(hossz) :
    turtle.forward(hossz)
#

def elso(h) :
    szakasz(h / 3.0)
    turtle.left(60)
    szakasz(h / 3.0)
    turtle.right(120)
    szakasz(h / 3.0)
    turtle.left(60)
    szakasz(h / 3.0)
#

def rekurziv(h, n) :
    
    if n == 0 :
        szakasz(h)
        return
    
    rekurziv(h / 3.0, n - 1)
    turtle.left(60)
    rekurziv(h / 3.0, n - 1)
    turtle.right(120)
    rekurziv(h / 3.0, n - 1)
    turtle.left(60)
    rekurziv(h / 3.0, n - 1)
#


def turtle_kezdes_hogy_kozepen_legyen(teljes_meret) :
    turtle.up()
    turtle.backward(teljes_meret / 2)
    turtle.down()
    turtle.width(2)
#


def main() :
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    teljes_meret = 600.0
    turtle.delay(0.9)
    
    turtle_kezdes_hogy_kozepen_legyen(teljes_meret)
    elso(teljes_meret)
    
    for i in range(6) :
        turtle.reset()
        turtle_kezdes_hogy_kozepen_legyen(teljes_meret)
        rekurziv(teljes_meret, i)
    
    turtle.mainloop()
    print(                         elvalaszto_sor                         )
    
#

# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#

