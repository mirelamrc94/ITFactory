
import random

# v1
def alege_castigator(participanti):

    index_castigator = random.randint(0, len(participanti) - 1)
    return index_castigator

#v2
def alege_castigator2(participanti):
    index_castigator = random.randint(0, len(participanti) - 1)
    return participanti[index_castigator]

if __name__ == '__main__':

    lista_participanti = ['Andrei', 'Ion', 'Dragos']
    #v1
    #ind_castigaor = alege_castigator(lista_participanti)
    #print(f'Castigatorul este {lista_participanti[ind_castigaor]}')

    #v2
    nume_castigator = alege_castigator2(lista_participanti)
    print(f'Nume castigator este {nume_castigator}')