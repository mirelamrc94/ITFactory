# o serie de functii care se exxecuta in ordine, oprinduse la prima functie daca indeplineste conditiile, daca nu,ruleaza pana se indeplineste una dintre contitiile numite

# x = int(input('x:'))
# if x >= 0:
#     print('X este nr natural')
# else:
#     print('Nu este nr natural')

# x = int(input('x:'))
# if x>0:
#     print('x este nr pozitiv')
# elif x<0:
#     print('x este nr negativ')
# else:
#     print('x este nr neutru')

# x = int(input('x:'))
# if x >= -2 and x <= 13:
#     print(f'x este {x} si se incadreaza criteriilor')
# else:
#     print(' x nu se incadreaza criteriilor')

# x = int(input('x:'))
# y = int(input('y:'))
# z = x-y
# if x - y < 5:
#     print(f'diferenta x-y este {z}')
# else:
#     print("diferenta este mai mare de 5")

# x = int(input('x:'))
# if not(x >= 5 and x <= 27):
#     print('x nu este intre 5 si 27')
# else:
#     print('x este cuprins intre 5 si 27 ')

# x = int(input('x:'))
# y = int(input('y:'))
# if  x == y:
#     print('Nr sunt egale')
# elif x > y:
#     print(f'{x} este mai mare')
# else:
#     print(f'{y} este mai mare')
#
# x = int(input('latura 1'))
# y = int(input('latura 2'))
# z = int(input('latura 3'))
# if (x == y or x == z or y == z) and not(x == y == z):
#     print('Triunghiul este isoscel')
# elif x == y == z:
#     print('Triunghiul este echilateral')
# else:
#     print('Tringhiul este oarecare')

# l = str(input('Tasteaza o litera'))
# if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
#     print('Litera este vocala')
# else:
#     print('Litera nu este vocala')

nota = int(input('Nota este:'))
if nota > 9 :
    print ('A')
elif nota > 8:
    print('B')
elif nota > 7:
    print('C')
elif nota > 6:
    print('D')
elif nota > 4:
    print('E')
else:
    print('F')


