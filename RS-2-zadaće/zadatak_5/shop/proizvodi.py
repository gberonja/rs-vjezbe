class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina
        
    def ispis(self):
        print(f"Proizvod: {self.naziv}, cijena: {self.cijena}, kolicina: {self.kolicina}")
        

proizvodi = [
    Proizvod("Mobitel", 500, 3),
    Proizvod("Računalo", 800, 2)
]

def dodaj_proizvod(naziv, cijena, kolicina):
    novi_proizvod = Proizvod(naziv, cijena, kolicina)
    proizvodi.append(novi_proizvod)
    
    