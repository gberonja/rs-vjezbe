from shop.proizvodi import proizvodi, dodaj_proizvod
from shop.narudzbe import napravi_narudzbu, narudzbe

novi_proizvodi = [
{"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
{"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
{"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
{"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for proizvod in novi_proizvodi:
    dodaj_proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["kolicina"])
    
for proizvod in proizvodi:
    proizvod.ispis()
    
napravi_narudzbu(novi_proizvodi)

# print(narudzbe)