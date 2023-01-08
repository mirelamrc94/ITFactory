#
# 1.
# Clasa Cerc
#
# Atribute: raza, culoare
#
# Constructor pt ambele atribute
#
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f'Culoarea cercului este {self.culoare} si raza este {self.raza}')

    def aria(self):
        arie_cerc = 3.14 * (self.raza ** 2)
        # print(f'Aria cercului este {arie_cerc}')
        return arie_cerc

    def diametru(self):
        diametru_cerc = self.raza * 2
        print(f'Diametrul cercului este {diametru_cerc}')

    def circumferinta(self):
        circumferinta_cerc = 2 * 3.14 * self.raza
        print(f'Circumferinta cercului este {circumferinta_cerc}')


# Clasa Dreptunghi
#
# Atribute: lungime, latime, culoare
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare
# si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(f'Dreptunghi cu lungime de {self.lungime}, latime de {self.latime}, culoare {self.culoare}')

    def arie_dreptunghi(self):
        arie = self.lungime * self.latime
        print(f'Aria dreptunghiului este de {arie}')

    def perimetru_dreptunghi(self):
        perimetru = 2 * ( self.lungime + self.latime)
        print(f'Perimetrul dreptunghiului este de {perimetru}')

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare
        #return self.culoare

class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu


    def descriere(self):
        print(f'Angajatul {self.nume} {self.prenume} are un salariu de {self.salariu} lei')

    def nume_complet(self):
        nume_complet = self.nume + " " + self.prenume
        return nume_complet

    def salariu_lunar(self):
        print(f'Salariul lunar al angajatului este de {self.salariu} lei')


    def salariu_anual(self):
        salariu = self.salariu * 12
        print(f'Salariul anual este {salariu} lei')

    def marire_salariu(self, procent):
        salariu = self.salariu * procent / 100 + self.salariu
        self.salariu = salariu
        print(f'Felicitari {self.nume_complet()}, salariul dvs a fost marit cu {procent} %, noul salariu fiind de {salariu} lei')


class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, suma):
        self.sold = self.sold - suma
        print(f'Ati retras suma de {suma}, noul sold este de {self.sold} lei ')

    def creditare_cont(self, suma):
        self.sold = self.sold + suma
        print(f'Ati alimentat cu {suma} lei, noul sold este {self.sold} lei')