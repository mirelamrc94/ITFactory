

class Animal:
    def __init__(self, nume, masa):
        self.nume = nume
        self.masa = masa

    def deplasare(self):
        print(1)
    def mananca(self):
        print(2)

class Pisica(Animal):

    def __init__(self, nume, masa, varsta, rasa, domestic):
        Animal.__init__(self, nume, masa)
        self.varsta = varsta
        self.rasa = rasa
        self.domestic = domestic # True sau False

    def deplasare(self):
        print(f'Pisica {self.nume} alearga')

    def mananca(self):
        print(f'Pisica {self.nume} mananca granule')

if __name__ == "__main__":

    a = Animal('Abc', 50)

    a.deplasare()
    a.mananca()

    p = Pisica('Kitty', 5, 3, 'xyz', True)
    p.deplasare()
    p.mananca()

