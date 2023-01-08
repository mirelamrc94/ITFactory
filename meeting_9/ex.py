
def func(x):
    return x ** 2

if __name__ == "__main__":

    #x = int(input("x="))

    #deschidem fisierul date.txt in modul de citire("r")
    f = open("date.txt", "r")
    #citim tot fisierul pe linii
    lines = f.readlines()
    print(lines)

    for line in lines:
        x = int(line)
        print(func(x))


    # #x = int(lines[0].replace("\n", ""))
    # x = int(lines[0])
    # #print(x)
    #
    # print(func(x))

    #cand nu mai avem nevoie de fisier, il inchidem
    f.close()

    g = open("date_iesire.txt", "w")

    for line in lines:
        x = int(line)
        g.write(str(func(x)) + "\n")

    g.close()

