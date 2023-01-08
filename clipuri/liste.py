# listele in py pot sa cuprinda elem de tipuri diferite
# au dimensiune dinamica
fructe = ['mar', 'banana', 'portocala',3 ,3, True]

# afisam o lista
print(fructe)

#accesam un elem in f de index
print(fructe[1])

#adaugam un nou elem
fructe.append('rosie')

#suprascriem
fructe[0] = 'para'

print(fructe)

#aflam dimensiunea
print(len(fructe))

# scoate si ne retuenaza ultimul elem
last = fructe.pop()
print("ultimul element" , last)
print('lista' , fructe)

#de cate ori apare un elem
print(fructe.count(3))
#extidem lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)

