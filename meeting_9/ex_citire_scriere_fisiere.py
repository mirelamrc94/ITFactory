import json

if __name__ == "__main__":

    f =open("dateinput.json", "r")
    d = json.load(f)
    f.close()

    print(d)
    print(type(d))
    print(d.keys())
    for key in d.keys():
        print(f"cheie={key}, valoare-{d[key]}")