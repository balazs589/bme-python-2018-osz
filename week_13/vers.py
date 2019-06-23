



def main() :
    
    
    
    vers = "Nem a regi s durva kozelites, / Mi szotol szoig igy kijon / betuiket szamlalva. / Ludolph eredmenye mar, / ha itt vegezzuk husz jegyen. / De rendre kijo meg tiz pontosan, / azt is bizvast igerhetem."
    
    szamjegyek = [len(szo.strip(",.")) for szo in vers.split() if szo != "/"]
    print(*szamjegyek, sep="")
#



if __name__ == "__main__" :
    main()
#