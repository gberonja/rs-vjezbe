import asyncio

async def autentifikacija(korisnik):
    asyncio.sleep(3)
    baza_korisnika = [
        {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
        {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
        {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
        {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
    ]
    
    for korisnik_info in baza_korisnika:
        if korisnik_info["korisnicko_ime"] == korisnik["korisnicko_ime"] and korisnik_info["email"] == korisnik["email"]:
            return await autorizacija(korisnik_info, korisnik["lozinka"])

    return f"Korisnik {korisnik} nije pronađen."

async def autorizacija(korisnik, lozinka):
    asyncio.sleep(2)
    baza_lozinka = [
        {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
        {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
        {'korisnicko_ime': 'maja_0x', 'email': 's324SDFfdsj234'},
        {'korisnicko_ime': 'zdeslav032', 'email': 'deso123'}
    ]
    for korisnik_info in baza_lozinka:
        if korisnik_info["korisnicko_ime"] == korisnik["korisnicko_ime"]:
            if korisnik_info["lozinka"] == lozinka:
                return f"Korisnik {korisnik["korisnicko_ime"]}: Autorizacija uspješna."
            else:
                return f"Korisnik {korisnik["korisnicko_ime"]}: Autorizacija neuspješna."
    
    return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."

async def main():
    korisnik_input = {
        "korisnicko_ime": "mirko123",
        "email": "mirko123@gmail.com",
        "lozinka": "lozinka123"
    }
    
    rezultat = await autentifikacija(korisnik_input)
    print(rezultat)
    
asyncio.run(main())
