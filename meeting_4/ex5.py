
#verificam daca nr este prim

nr = int(input('nr='))

nr_este_prim = True # presupunem ca nr este prim pana la proba contrarie
for i in range (2, nr//2 + 1):
    if nr % i == 0: # daca am gasit un divizor in interlalul (2 , nr/2)
        nr_este_prim = False #marchez ca nr nu este prim
        print (f'{nr} nu este prim pentru ca se imparte exact la {i}')
        break
if nr_este_prim :
    print(f'{nr} este prim!')