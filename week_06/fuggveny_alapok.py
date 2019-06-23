"""

"""


# =============================================================================

import math


# =============================================================================
# a feladat megoldasahoz letrehozott fuggvenyek

# docstring style:
# http://www.sphinx-doc.org/en/1.5/ext/example_google.html

# -----------------------------------------------------------------------------
def kob(x) :
    """Fuggveny ami meghatarozza egy valos szam harmadik hatvanyat.
    
    Args:
        x (float): Valos szam, aminek a harmadik hatvanyat szamoljuk.
       
    Returns:
        float: x^3
    
    Raises:
        ValueError: Ha valos szamkent nemertelmezheto az input
    
    Hasznalat:
    
    >>> y = kob(x=2.0)
    """
    
    return x ** 3
    
# end kob

# -----------------------------------------------------------------------------
def abszolut(x) :
    """Fuggveny ami meghatarozza egy valos abszoluterteket.
    
    Args:
        x (float): Valos szam, aminek az abszoluterteket meghatarozzuk.
       
    Returns:
        float: |x| = abs(x)
    
    Hasznalat:
    
    >>> y = abszolut(x=-2.0)
    """
    
    if x < 0.0 :
        return -x
    else :
        return x
# end abszolut


# -----------------------------------------------------------------------------
def main() :
    """
    Program futtatasa.
    """
    kezdet = -1.0
    veg =  1.0
    lepeskoz = 0.1
    
    a = kezdet
    while a <= veg :
        print("{:10.4f}{:10.4f}{:10.4f}{:10.4f}".format(a, kob(a), abszolut(a), math.sin(a)))
        a += lepeskoz
    # end while
    
# end main

# =============================================================================


main()





