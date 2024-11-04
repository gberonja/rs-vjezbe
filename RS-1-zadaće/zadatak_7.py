def provjera_lozinke(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
    elif not (any(slovo.isupper() for slovo in lozinka) and any(slovo.isdigit() for slovo in lozinka)):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
    elif("password" in lozinka.lower() or "lozinka" in lozinka.lower()):
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
    else:
        print("Lozinka je jaka!")

provjera_lozinke("evonekAlozinka423")