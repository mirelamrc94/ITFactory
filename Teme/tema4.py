# 1.
# Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

#for masina in masini:
#    print(f"Masina mea preferata este {masina}")

# i = 0
# while i < len(masini):
#     print(f'Masina mea preferata este {masini[i]}')
#     i += 1


# Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’
# Faceti acelasi lucru cu un for each
# Faceti acelasi lucru cu un while

# 2.
# Aceeasi lista
# Folositi un for
# In for
#    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# Printati varianta finala a listei
#
# print(masini)
#
# for masina in masini:
#     if masina == masini[0] or masina == masini[-1]:
#         print(masina)
#     else:
#         print(masina.upper())


# 3.
# Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin for each
# Daca masina e mercedes (if)
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam

# print(masini)
#
# for masina in masini:
#     if masina == 'Mercedes':
#         print('Am gasit masina dorita de dvs!')
#         break
#     else:
#         print(f'Am gasit masina {masina}, mai cautam')


# 4.
# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x

# print(masini)
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lastun':
#         continue
#     else:
#         print(f'S-ar putea sa va placa masina {masina}!')

# Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)  -- nu stiu
# Printati Modele vechi: x
# Modele noi: x


# masini_vechi = []
#
# for masina in masini:
#     if masina == 'Lastun' or masina == 'Trabant':
#         masini_vechi.append(masina)
#
# print(f'Modele vechi:{masini_vechi}')
# print(f'Modele noi: {masini}')


# # 6.
# Avand dict

# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista

# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# for i in pret_masini:
#     if pret_masini.get(i) > 15000:
#         print(i)
#
# print(pret_masini.items())
# for i in pret_masini.items():
#         if i[1]<15000:
#            print(f'Pentru un buget de sub 15000 de euro puteti alege masina {i[0]}')


# 7.
# Avand lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # Iterati prin ea
# # Afisati de cate ori apare 3
# # (nu aveti voie sa folositi count)
#
# print(numere)
# nr = 0
# for i in numere:
#     if i == 3:
#         nr += 1
# print(f" Numarul 3 apare de {nr} ori in lista")


# 8.
# Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)

# print(numere)
# i = 0
# for nr in numere:
#     i = i + nr
# print(f"suma nr din lista este {i}")

# 9.
# Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)

# print(numere)
# i = 0
# for nr in numere:
#     if nr > i:
#         i = nr
# print(f"cel mai mare nr din lista este {i}")

#
# 10.
# Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

# print(numere)
# for nr in range (len(numere)):
#     if numere[nr] > 0:
#         numere[nr] = numere[nr] * -1
#     else:
#         numere[nr] = abs(numere[nr])
# print(numere)

