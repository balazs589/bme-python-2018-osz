

# Alakitsd az alabbi programreszeket list comprehension kifejezesse!


def main() :
    
    #l = []
    #for i in range(0, 10):
    #    l.append(i * 2)
    
    l = [i *2 for i in range(0, 10)]
    print(l)
    
    
    #l = []
    #for i in range(100):
    #    if i % 10 == 3:
    #        l.append(i)
    
    l = [i for i in range(100) if i % 10 == 3]
    print(l)
    
    
    #l1 = [43, 15, 48, 59, 33, 72, 11, 65, 95, 34]
    #l2 = []
    #for i in l1:
    #    if i % 2 == 1:
    #        l2.append(i)
    
    l1 = [43, 15, 48, 59, 33, 72, 11, 65, 95, 34]
    l2 = [i for i in l1 if i % 2 == 1]
    print(l2)
    
    
    
    #l1 = [43, 15, 48, 59, 33, 72, 11, 65, 95, 34]
    #l2 = []
    #for i in l1:
    #    if i % 2 == 1:
    #        l2.append(True)
    #    else:
    #        l2.append(False)
    ## Vigyazz, ebben atveres az if.
    
    l1 = [43, 15, 48, 59, 33, 72, 11, 65, 95, 34]
    l2 = [i % 2 == 1 for i in l1]
    print(l2)
    
    
    #l1 = ["alma", "korte", "barack", "szilva", "ananasz"]
    #l2 = []
    #for s in l1:
    #    if s[0] == 'a':
    #        l2.append(s)
    
    l1 = ["alma", "korte", "barack", "szilva", "ananasz"]
    l2 = [s for s in l1 if s[0] == "a"]
    print(l2)
    
    
    
    #l1 = ["alma", "korte", "barack", "szilva", "meggy"]
    #l2 = []
    #for s in l1:
    #    l2.append(len(s))
    
    l1 = ["alma", "korte", "barack", "szilva", "meggy"]
    l2 = [len(s) for s in l1]
    print(l2)
#



if __name__ == "__main__" :
    main()
#


