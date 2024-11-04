# Vježba 14
def isPrime(a):
    if a <= 1:
        return False
    for i in range (2, int(a**0.5)+1): # provjera djeljivosti od 2 do kvadratnog korijena broja
        if a%i==0:
            return False
    return True

print(isPrime(7))