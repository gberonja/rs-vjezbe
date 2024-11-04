# Vježba 13.1
def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])

#print(prvi_i_zadnji([1,2,3,4,5,6]))

# Vježba 13.2
def maks_i_min(lista):
    maks = lista[0]
    min = lista[0]
    
    for broj in lista:
        if broj > maks:
            maks = broj
        if broj < min:
            min = broj
    return(maks, min)

#print(maks_i_min([1,2,3,4,5]))

# Vježba 13.3
def presjek(skup_1, skup_2):
    return skup_1 & skup_2

print(presjek({2,3,4},{4,5,3}))