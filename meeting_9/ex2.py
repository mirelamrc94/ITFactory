
def func(x):
    return x ** 2

if __name__ == "__main__":

    # deschidem fisierul date.txt in modul de citire("r")
    with open("date.txt", "r") as f: #f = open("date.txt", "r")
        # citim tot fisierul pe linii
        lines = f.readlines()
        #la sfarsitul lui with, se va face f.close automat

    print(lines)

    for line in lines:
        x = int(line)
        print(func(x))


