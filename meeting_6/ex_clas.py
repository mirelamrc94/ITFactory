
class Engine:

    def __init__(self, engine_name='ceva'):
        self.name = engine_name

class Car:

    def __init__(self, marca_p, model_p, culoare_p='white', an_productie_p=2015,engine_p = None):
        self.marca = marca_p
        self.model = model_p
        self.culoare = culoare_p
        self.an_productie = an_productie_p
        self.ignition = 'off'
        self.engine = engine_p
        self.lista_revizii = []

    #metoda pt a porni masina

    def start(self):
        print(f'Masina {self.mode} a pornit!')
        self.ignition = 'on'

    #metoda pentru a opri masina
    def stop(self):
        print(f'Masina {self} s-a oprit')
        self.ignition = 'off'

    #metoda pentru a verifica starea de pornit/opriit
    def print_ignition_state(self):
if __name__ == "__main__":
    c1 = Car('Dacia', 'Spring', 'gri', 2022)
    c2 = Car('Vw', 'Golf', 'yellow', 2019)

    lista_masini = []
    lista_masini.append(c1)
    lista_masini.append(c2)


    #for c in lista_masini:
    #varianta 1 cu indecsi
    for i in range(len(lista_masini)):
        print(f'Masina cu indexul {i}: {lista_masini[i].marca} {lista_masini[i].model} '
              f'{lista_masini[i].culoare} {lista_masini[i].an_productie}')

    # varianta 2 fara indecsi
    for c in lista_masini:
        print(f"Masina: {c.marca} {c.model} {c.culoare} {c.an_productie}")


    # print(type(c1))
    # print(c1.model)
    # print(c1.culoare)
    # print(c1.an_productie)
    # print(c1.marca)


