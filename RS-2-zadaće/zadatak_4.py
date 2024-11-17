# 4.1.
from datetime import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza
        
    def ispis(self):
        return f"Ovo je automobil {self.marka} {self.model}, proizveden {self.godina_proizvodnje} i prešao je {self.kilometraza} kilometara."
        
    def starost(self):
        return f"Automobil je star {datetime.now().year - self.godina_proizvodnje} godine."
        
        
auto = Automobil("Mercedes-Benz", "124", 1990, 300000)

print(auto.ispis())
print(auto.starost())        

# 4.2.

class Kalkulator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        if self.b == 0:
            return "Ne može se dijeliti s nulom"
        return self.a / self.b
    
    def potenciranje(self):
        return self.a ** self.b
    
    def korijen(self):
        if self.a < 0 and self.b % 2 == 0:
                return "Područje kompleksnih brojeva"
        if self.b == 0:
                return "Ne može se izračunati nulti korijen"
        return self.a ** (1/self.b)
    
# 4.3.
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
        
    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)
    
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]
    
studenti_objekti = [Student(student["ime"], student["prezime"], student["godine"], student["ocjene"]) for student in studenti]

najbolji_student = max(studenti_objekti, key = lambda student: student.prosjek())

print(f"Najbolji student/studentica je {najbolji_student.ime} {najbolji_student.prezime} s prosjekom ocjena {najbolji_student.prosjek()}")
        
# 4.4.
import math

class Krug:
    def __init__(self, r):
        self.r = r
        
    def opseg(self):
        return 2 * math.pi * self.r
    
    def povrsina(self):
        return math.pi * self.r**2

krug = Krug(5)

print(krug.opseg())
print(krug.povrsina())

# 4.5.
class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
        
    def work(self):
        return f"Radim na poziciji {self.pozicija}"
    
    def povecanje_place(self, povecanje):
        self.placa += povecanje
        
class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
        
    def work(self):
        return f"Radim na poziciji {self.pozicija} u odjelu {self.department}"
    
    def give_raise(self, radnik, povecanje):
        radnik.povecanje_place(povecanje)
        

radnik = Radnik("Ivan", "konobar", 1000)
print(radnik.work())

menadzer = Manager("Ante", "voditelj smjene", 1500, "ugostiteljstvo")
print(menadzer.work())
menadzer.give_raise(radnik, 200)