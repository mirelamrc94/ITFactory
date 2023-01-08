
def este_prim(nr):
    nr_este_prim = True  # presupunem ca nr este prim pana la proba contrarie
    for i in range(nr // 2 + 1):
        if i == 0 or i == 1:  # daca am gasit un divizor in interlalul (2 , nr/2)
            continue
        if nr % i == 0:
            nr_este_prim = False  # marchez ca nr nu este prim
            print(f'{nr} nu este prim pentru ca se imparte exact la {i}')
            break
    return nr_este_prim

if __name__ == "__main__":
#aflam un nr prim

    x = int(input('nr='))
    x_este_prim = este_prim(x)

    if x_este_prim :
        print(f'{x} este prim!')
