from pydantic import BaseModel

class Automobil(BaseModel):
    id: int
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str

class CreateAutomobil(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str