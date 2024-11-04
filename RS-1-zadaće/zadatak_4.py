broj = 0
while broj < 5:
    broj +=2
    print(broj) # ispisati će brojeve 2 i 4
    
broj = 0
while broj < 5:
    broj += 1
    print(broj)
    broj -= 1
    
# svaki put kada broj prolazi petlju, poveća mu se vrijednost za 1 i smanji za 1

broj = 10
while broj > 0:
    broj -= 1
    print(broj)
    if broj < 5:
        broj += 2
        
# petlja će funkcionirati do broja 4, onda će se stalno mijenjati vrijednost 6,5,4
    