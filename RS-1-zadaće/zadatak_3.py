from random import randint

def pogodi_broj():
    ciljni_broj = randint(1,100)
    broj_je_pogoden = False
    broj_pokusaja = 1 # Pokušaji kreću od 1, ne od 0
    
    while not broj_je_pogoden:
        uneseni_broj = int(input("Unesite broj od 1 do 100: "))
        
        if(uneseni_broj == ciljni_broj):
            print(f"Bravo, pogodio si u {broj_pokusaja} pokušaja")
            broj_je_pogoden = True
        elif(uneseni_broj < ciljni_broj):
            print("Uneseni broj je manji od ciljnog broja")
            broj_pokusaja += 1
        else:
            print("Uneseni broj je veći od ciljnog broja")
            broj_pokusaja += 1

pogodi_broj()