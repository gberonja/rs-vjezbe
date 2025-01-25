from aiohttp import web
import hashlib

korisnici = [
    {"korisnicko_ime": "admin", "lozinka_hash" :
    "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"}, 
    # lozinka = "lozinka123"
    {"korisnicko_ime": "markoMaric", "lozinka_hash" :
    "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"}, 
    # lozinka = "markoKralj123"
    {"korisnicko_ime": "ivanHorvat", "lozinka_hash" :
    "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"}, 
    # lozinka = "lllllllllllozinka_123"
    {"korisnicko_ime": "Nada000",
    "lozinka_hash":"492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"} 
    #lozinka = "blablabla"
]

def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

async def register(request):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return web.json_response({"error": "Potrebni su korisničko ime i šifra"}, status=404)
    
    for korisnik in korisnici:
            if korisnik["korisnicko_ime"] == username:
                return web.json_response({"error": "Korisnik već postoji"}, status=400)

    novi_korisnik = {
        "korisnicko_ime": username,
        "lozinka_hash": hash_data(password)
    }
    korisnici.append(novi_korisnik)
    return web.json_response({"message": f"Korisnik {username} je registriran"},status=200)

async def login(request):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return web.json_response({"error": "Potrebni su korisničko ime i šifra"}, status=404)
    
    for korisnik in korisnici:
            if korisnik["korisnicko_ime"] == username:
                if korisnik["lozinka_hash"] == hash_data(password):
                    return web.json_response({"message": f"Korisnik {username} uspješno prijavljen"})
                else:
                    return web.json_response({"error": "Pogrešna lozinka"}, status=401)

    return web.json_response({"error": "Korisnik ne postoji"}, status=404)


async def dummy_login(request) -> bool:
    data = await request.json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return False

    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == username and korisnik["lozinka_hash"] == hash_data(password):
            return True

    return False


app = web.Application()
app.router.add_post("/register", register)
app.router.add_get("/login", login)
app.router.add_post("/dummy_login", dummy_login)

if __name__ == "__main__":
    web.run_app(app, port=9000)