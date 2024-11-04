def brojanje_rijeci(tekst):
    tekst = tekst.lower() 
    for znak in ".,!?;:": # moguće dodati i još simbola
        tekst.replace(znak, "")
        
    rijeci = tekst.split()
    rjecnik = {}
    
    for rijec in rijeci:
        if rijec in rjecnik:
            rjecnik[rijec] += 1
        else:
            rjecnik[rijec] = 1
    return rjecnik
    
print(brojanje_rijeci("Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."))
    
    