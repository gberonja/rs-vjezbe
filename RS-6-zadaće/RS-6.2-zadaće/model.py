from pydantic import BaseModel
from typing import Optional, List, Literal, TypedDict, Tuple
from datetime import datetime


# Zadatak 1
class Izdavac(BaseModel):
    naziv: str
    adresa: str

class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: Optional[int] = datetime.now().year
    broj_izdavanja: int
    izdavac: Izdavac
    
# Zadatak 2
class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: List[Literal["dodavanje" , "brisanje" , "ažuriranje" , "čitanje"]]
    
# Zadatak 3
class Jelo(BaseModel):
    identifikator: int
    naziv: str
    cijena: float
    
class StolInfo(TypedDict):
    broj: int
    lokacija: str

class RestaurantOrder(BaseModel):
    identifikator: int
    ime_kupca: str
    stol_info: StolInfo
    lista_jela: List[Jelo]
    ukupna_cijena: float

# Zadatak 4
class CCTV_frame(BaseModel):
    identifikator: int
    vrijeme_snimanja: datetime
    koordinate: Optional[Tuple[float,float]] = (0.0,0.0)