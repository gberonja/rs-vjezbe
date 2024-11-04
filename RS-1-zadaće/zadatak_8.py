def filtriraj_parne(lista):
    nova_lista = []
    for broj in lista:
        if broj % 2 == 0:
            nova_lista.append(broj)
    return nova_lista

print(filtriraj_parne([1,2,3,4,5,6]))