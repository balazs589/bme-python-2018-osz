
class BinFa:
    def __init__(self, ertek):
        self.ertek  = ertek
        self.bal    = None
        self.jobb   = None
#

def beszur(gyoker, ertek):
    if gyoker is None:
        gyoker          = BinFa(ertek)
    elif ertek < gyoker.ertek:
        gyoker.bal      = beszur(gyoker.bal, ertek)
    elif ertek > gyoker.ertek:
        gyoker.jobb     = beszur(gyoker.jobb, ertek)
    else:
        pass
    return gyoker
#


def main():
    tesztadat = [15, 96, 34, 12, 14, 56, 21, 11, 10, 9, 78, 43]
    gyoker = None
    for x in tesztadat:
        gyoker = beszur(gyoker, x)
#

if __name__ == "__main__" :
    main()
#


