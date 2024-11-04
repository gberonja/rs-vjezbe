def kalkulator():
    a = float(input("Unesite prvi broj: "))
    b = float(input("Unesite drugi broj: "))
    operator = input("Unesite operator (+,-,*,/): ")
    
    operators = {
        "+": lambda a,b:a+b,
        "-": lambda a,b:a-b,
        "*": lambda a,b:a*b,
        "/": lambda a,b:a/b if b !=0 else "Dijeljenje s nulom nije dozvoljeno!"
    }
    
    if operator not in operators:
        print("Nepodržani operator!")
    else:
        result = operators[operator](a,b)
        print(f"Rezultat operacije {a} {operator} {b} je {result}")
        
kalkulator()
