def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    rjecnik = {
        'vowels': 0,
        'consonants': 0
    }
    
    for znak in tekst:
        if znak in vowels:
            rjecnik['vowels'] += 1
        if znak in consonants:
            rjecnik['consonants'] += 1
            
    return rjecnik

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(count_vowels_consonants(tekst))