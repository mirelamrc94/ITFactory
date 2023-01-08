'''
Flow control - if else
evalueaza conditii si bifurca codul in fucntie de rezultat
'''

piesa_faina= True

print('pornim radio')
if piesa_faina == False:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else

#daca nr este par, printam acest lucru
#altfel printam impar

nr = 3

# ce inseamna par? se imparte exact ;a 2
# ce inseamna ca se imparte la 2? impartirea ne da restul 0
if nr % 2 == 0:
    print ('nr par')
else:
    print('nr impar')


#este un nr pozitiv?
if ( nr > 0):
    print('pozitiv')
else:
    print(' nr nu este pozitiv')

# daca are sun 18 ani nu poate paria, altfel poate  -tema

#if, else if, else
# cum ne saluta robotelul in fuctie de ora?
#luam date de la tastatura
#ne asiguram ca sunt transfortmate din sring in int
# ora = int(input('Introdu ora'))
# if ora < 0:
#     print('ora invalida. ora negativa')
# elif ora <= 11:
#     print('buna dimineata')
# elif ora <= 18:
#     print('buna ziua')
# elif ora <= 21:
#     print('buna seara')
# elif ora <= 24:
#     print('noapte buna')
# else:
#     print('ora invalida. ora mai mare decat 24')

# CTRL + /
# robotel telefonic
optiune = int(input('Alege o optiune'))
if optiune == 0 :
    print('meniu principal')
elif optiune == 1:
    print('ati ales romana')
elif optiune == 2:
    print('ati ales engleza')
else:
    print(' nua m identidicat optiunea, mai incearca')