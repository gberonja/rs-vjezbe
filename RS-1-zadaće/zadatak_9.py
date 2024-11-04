def ukloni_duplikate(lista):
    nova_lista = []
    for broj in lista:
        if broj not in nova_lista:
            nova_lista.append(broj)
            
    return nova_lista

print(ukloni_duplikate([1,2,3,4,1,2]))