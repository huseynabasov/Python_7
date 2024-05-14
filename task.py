import random
import math

def kvadrat():
    newlist = []
    for i in range(5):
        rand = random.randint(20,50)
        newlist.append(rand) 
    print(f"Random secilmis 5 reqemden ibaret list: {newlist}")
    
    cutlist = []
    for i in newlist:
        if i % 2 == 0:
            cutlist.append(math.pow(i, 2))
    print(f"Kvadrata yukseldilmis cut reqemler: {cutlist}")
    # newlist.append(rand)
kvadrat()
 
