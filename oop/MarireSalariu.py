
class Angajat:
    def __init__(self, nume, prenume, salariu, vechime, functie):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        self.vechime = vechime
        self.functie = functie

    def DescriereAngajat(self):
        print(f'Angajatul {self.nume} {self.prenume}')
        print(f'Salariu {self.salariu}')
        print(f'Vechime {self.vechime}')
        print(f'Functia de = {self.functie}')
        print('-----------------------------')

    def MarireSalariu(self):
        print(f'Angajatul {self.nume} {self.prenume} va primi o marire de salariu in valoare de:')
        if self.vechime < 5:
            self.salariu += 300
            print('Ati primit o marire de salariu de 300 lei!')
        else:
            self.salariu += 500
            print('Ati primit o marire de salariu de 500 lei!')

    def ActualizareVechime(self, numar):
        noua_vechime = self.vechime + numar
        self.vechime = noua_vechime
        print(f'Noua vechime a angajatului {self.nume} este {self.vechime}')





