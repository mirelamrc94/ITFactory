#
#
# # 1. Functie care sa calculeze si sa returneze suma a 2 numere
#
# def suma(a,b):
#     rez = a + b
#     return rez
#
# if __name__ == '__main__':
#     # a = int(input('a = '))
#     # b = int(input('b = '))
#     total = suma(2, 6)
#     total2 = suma(120, 260)
#     print(f'Suma celor 2 numere este {total}')
#     print(f'Suma celorlalte 2 numere este {total2}')

# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

# def nr_pare(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#     nr_par = nr_pare(20)
#     nr_impar = nr_pare(33)
#     print(nr_par)
#     print(nr_impar)

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)

# def nr_caract(nume):
#     tot_caract = nume.replace(" ", "")
#     return len(tot_caract)
#
# if __name__ == '__main__':
#     #nume_intreg = 'Mariana Popescu'
#     nume_intreg2 = 'Ana Maria Nistor Alupului'
#
#    # nr_tot_caract = nr_caract(nume_intreg)
#     nr_tot_caract = nr_caract(nume_intreg2)
#
#     print(nr_tot_caract)
#
#4. Functie care returneaza aria dreptunghiului

# def arie_dreptunghi(lungime, latime):
#     arie = lungime * latime
#     return arie
#
# calcul_arie1 = arie_dreptunghi(5, 3)
# calcul_arie2 = arie_dreptunghi(153, 282)
# print(calcul_arie1)
# print(calcul_arie2)

# 5. Functie care returneaza aria cercului

# def arie_cerc(diametru):
#     pi = 3.14
#     raza = diametru_cerc / 2
#     arie = pi * (raza ** 2)
#     return arie
#
# diametru_cerc = int(input('Diametrul cercului: '))
# calcul_arie = arie_cerc(diametru_cerc)
# print(calcul_arie)

# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

# def gaseste_caracter(caract):
#     if caract in string:
#         return True
#     else:
#         return False
#
# caracter = input('Introdu un caracter: ')
# string = 'Ana are mere rosii.'
#
# caracter_selectat = gaseste_caracter(caracter)
# print( caracter_selectat)


# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y

def caractere_lower_upper(text):
    caract_upper = 0
    caract_lower = 0
    for i in text:
        if (i.ispupper()):
            caract_upper += 1
        elif (i.islower()):
            caract_lower += 1
    return







# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
#
# 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.
#
# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

