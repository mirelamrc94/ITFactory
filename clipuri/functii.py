
def printGreeting():
    print('Buna ziua, bine ati venit!')

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')

def mediaNr(a, b, c):
    return (a + b + c) / 3

def piValue():
    return  3.14
    print('abc')


#exercitiu
# daca pers e majora, altfel false
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False





#zona de apelare(desktop)
# printGreeting()
# printGreeting()
# printGreetingByName('Sinpetrean', 'Andy')
# printGreetingByName('Sinpetrean', 'crina')
# printGreetingByName('Sinpetrean', 'ares')
# print(mediaNr(3,3,4))
# print(piValue())
# print(verificareMajor(18))
#
# # se ia varsta utilizatorului
#
# age = int(input('introduceti varsta dvs'))
#
# if verificareMajor(age):
#     print('Cont creat. Bine ai venit in aplicatie')
# else:
#     print('Nu ai varsta minima necesara (18) pt a paria')


# oop
# variabile => atribute, proprietati sau fields
# functii => metode

#avand 3 nr returnati pe cel mai mare

def NrMax(a, b, c):
    return max(a, b, c)


print(NrMax(4,5,41))

