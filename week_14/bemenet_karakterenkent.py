"""
"""

# -----------------------------------------------------------------------------
# import:
import sys


# -----------------------------------------------------------------------------
# fuggvenyek:


def main() :
    
    
    elvalaszto_sor = "\n" + ("-" * 79) + "\n"
    print(                         elvalaszto_sor                         )
    
    
    
    while True :
        c = sys.stdin.read(1)
        if c == "" :
            break
        else :
            print(ord(c))
    print("Bemenet vege.")
    
    print(                         elvalaszto_sor                         )
    
#


# -----------------------------------------------------------------------------
# futtatas:

if __name__ == "__main__" :
    main()
#

