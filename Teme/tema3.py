#
# #1
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
#
# print(note_muzicale)
# note_muzicale = note_muzicale[::-1]
# print(note_muzicale)
#
# note_muzicale.reverse()
# print(note_muzicale)
#
# #2
# print(note_muzicale.count('do'))
#
# 3
#
# l1 = [3, 1, 0, 2]
# l2 = [6, 5, 4]
#
# l1.extend(l2)
# print(l1)
# #l1.append(l2)
# #print(l1)
#
# #4
# # l1.sort()
# # print(l1)
# # l1.sort()
# # Sorteaza nr 0? nu stiu
#
# #5
#
# i = len(l1)
# if i > 0:
#     print('Lista nu este goala')
# else:
#     print('Lista este goala')
#
#
# #6
#
# l1.clear()
# print(l1)
#
# #7
#
# i = len(l1)
# if i > 0:
#     print('Lista nu este goala')
# else:
#     print('Lista este goala')
#
# 8

dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}

print(dict1.keys())

#9

print(f'Ana a luat nota: {dict1["Ana"]} ')

#10

dict1['Dorel'] = 6

print(dict1['Dorel'])

#11

dict1['Ionica'] = dict1.pop('Gigel')
dict1['Ionica'] = 9

print(dict1)

#extra

jucatori = ['Alex', 'Alin', 'Laur', 'Robi', 'Bobi']

schimbari_efectuate = 2
schimbari_max = 3

