def fakt_for():
    a = int(input("Unesite broj: "))
    if a < 2:
        print(f"Faktorijel od {a} je 1")
    else:
        faktorijel = 1
        for i in range(2,a+1):
            faktorijel *= i
        print(f"Faktorijel od {a} je {faktorijel}")
        
# fakt_for()

def fakt_while():
    a = int(input("Unesite broj: "))
    if a < 2:
        print(f"Faktorijel od {a} je 1")
    else:
        faktorijel, i = 1, 1
        while i <= a:
            faktorijel *= i
            i += 1
        print(f"Faktorijel od {a} je {faktorijel}")
        
fakt_while()