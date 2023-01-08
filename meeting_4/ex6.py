
l = [ 1,2,5,6,99,90,123,124]

# verificam daca contine doar nr pozitive

i = 0
while i < len(l):
    if l[i] < 0:
        print('lista contine cel putin un nr negativ')
        break
    i += 1
