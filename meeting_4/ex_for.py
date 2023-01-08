

l = [1,2,5,6,99,90,123,124]

#afisam nr pare din lista

#modul 1

for ind in range(len(l)):
    if l[ind] % 2 == 0:
        print(l[ind])
else:
    print("am terminat bucla for!")


#modul 2

for elem in l:
    if elem % 2 == 0:
        print(elem)
else:
    print('Am terminat bucla for!')

