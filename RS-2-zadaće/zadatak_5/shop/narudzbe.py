class Narudzba:
    def __init__(self, proizvodi, ukupna_cijena):
        self.proizvodi = proizvodi
        self.ukupna_cijena = ukupna_cijena
        
    def ispis_narudzbe(self):
        narudzba_info = ", ".join(f"{proizvod['naziv']} x {proizvod['kolicina']}" for proizvod in self.proizvodi)
        print(f"Naručeni proizvodi: {narudzba_info} ,Ukupna cijena: {self.ukupna_cijena} eur")
        
def napravi_narudzbu(lista_proizvoda):
    potrebni_kljucevi = {"naziv", "cijena", "kolicina"}
    ukupna_cijena = 0
    
    # argument proizvodi mora biti lista
    if not isinstance(lista_proizvoda, list):
        print("Argument proizvodi mora biti lista")
        return None
    # lista ne smije biti prazna
    if not lista_proizvoda:
        print("Lista ne smije biti prazna")
        return None
    for proizvod in lista_proizvoda:
        # svaki element u listi mora biti rječnik
        if not isinstance(proizvod, dict):
            print("Svaki element u listi mora biti rječnik")
            return None
        # svaki rječnik mora sadržavati ključeve Qnaziv , cijena i kolicina
        if not potrebni_kljucevi.issubset(proizvod.keys()):
            print("Svaki rječnik mora sadržavati ključeve naziv , cijena i kolicina")
            return None
        if proizvod["kolicina"] == 0:
            print(f"Proizvod {proizvod['naziv']} nije dostupan!")
            return None
        ukupna_cijena += proizvod['cijena'] * proizvod['kolicina']
        
    narudzba = {
        "proizvodi": lista_proizvoda,
        "ukupna_cijena": ukupna_cijena
    }
    
    narudzbe.append(narudzba)
    
    
narudzbe = []