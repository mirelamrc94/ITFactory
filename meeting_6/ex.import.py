

from ex_clas import Car, Engine


if __name__ == "__main__":

    c = Car("BMW", 'XS', 'gri', 2020)
    d = Car ('Volvo', 'XC50')

    print(c.marca)
    print(c.model)
    print(c.culoare)
    print(c.an_productie)
    print(d.marca)
    print(d.model)
    print(d.culoare)
    print(d.an_productie)

    #metoda pt a porni masina

    def start(self):
        print(f'Masina {self.mode} a pornit!')
        self.ignition = 'on'

    #metoda pentru a opri masina
    def stop(self):
        print(f'Masina {self} s-a oprit')




