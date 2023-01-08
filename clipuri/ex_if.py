
nota1 = int(input('nota1= '))
nota2 = int(input('nota2= '))

#print(type(nota1))
#print(type(nota2))

#calculam media arintmetica

media_aritmetica = (nota1 + nota2) / 2
print(media_aritmetica)
'''
if media_aritmetica >= 5:
    print ('Felicitari! Ai promovat')
else:
    print ('nu ai promovat!')
'''

if media_aritmetica >= 8:
    print('Felicitari! Ai promovat cu nota mare!')
elif media_aritmetica >= 5: # and media_aritmetica < 8
    print('Ai promovat!')
else:
    print('Nu ai promovat!')

