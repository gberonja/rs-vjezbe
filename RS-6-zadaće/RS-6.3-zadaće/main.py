from fastapi import FastAPI, HTTPException,Query
from models import Automobil, CreateAutomobil
from typing import Optional, List

app = FastAPI()

# Početni podaci
automobili = [
    Automobil(id=1, marka="Toyota", model="Corolla", godina_proizvodnje=2020, cijena=20000, boja="crvena"),
    Automobil(id=2, marka="Honda", model="Civic", godina_proizvodnje=2019, cijena=18000, boja="plava"),
    Automobil(id=3, marka="Ford", model="Focus", godina_proizvodnje=2021, cijena=22000, boja="crna"),
]

@app.get("/automobili", response_model=List[Automobil])
def dohvati_automobile(
    min_cijena: Optional[float] = Query(0, ge=0),
    max_cijena: Optional[float] = Query(None),
    min_godina: Optional[int] = Query(1960, ge=1960),
    max_godina: Optional[int] = Query(None)
):
    if max_cijena is not None and min_cijena > max_cijena:
        raise HTTPException(status_code=400, detail="Minimalna cijena ne može biti veća od maksimalne cijene.")
    if max_godina is not None and min_godina > max_godina:
        raise HTTPException(status_code=400, detail="Minimalna godina ne može biti veća od maksimalne godine.")
    
    filtrirani_automobili = [
        auto for auto in automobili
        if auto.cijena >= min_cijena and (max_cijena is None or auto.cijena <= max_cijena)
        and auto.godina_proizvodnje >= min_godina and (max_godina is None or auto.godina_proizvodnje <= max_godina)
    ]
    return filtrirani_automobili

@app.get("/automobil/{auto_id}", response_model=Automobil)
def dohvati_automobil(auto_id: int):
    for auto in automobili:
        if auto.id == auto_id:
            return auto
    raise HTTPException(status_code=404, detail="Automobil nije pronađen")

@app.post("/automobili", response_model=Automobil)
def dodaj_auto(auto: CreateAutomobil):
    for postojece_auto in automobili:
        if (
            postojece_auto.marka.lower() == auto.marka.lower()
            and postojece_auto.model.lower() == auto.model.lower()
            and postojece_auto.godina_proizvodnje == auto.godina_proizvodnje
        ):
            raise HTTPException(status_code=400, detail="Automobil već postoji u bazi podataka.")
    
    new_id = len(automobili) + 1
    auto_s_id = Automobil(id=new_id, **auto.dict())
    automobili.append(auto_s_id)
    return auto_s_id