def grupiraj_po_paritetu(lista):
    rjecnik = {
        'parni': [],
        'neparni': []
    }
    
    for broj in lista:
        if broj % 2 == 0:
            rjecnik['parni'].append(broj)
        else:
            rjecnik['neparni'].append(broj)
            
    return rjecnik

print(grupiraj_po_paritetu([1,2,3,4,5,6,7,8]))