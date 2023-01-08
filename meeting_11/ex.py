
import csv
import json

#exemplu adapter pattern
#de la format csv la format json
if __name__ == '__main__':

    f = open("input.csv", "r")
    g = open("output.json", "w")

    my_dict = {}

    csv_reader = csv.reader(f)

    counter = 0
    for row in csv_reader:
        my_dict[counter] = row
        counter += 1

    output = json.dumps(my_dict, indent=2)
    g.write(output)

    f.close()
    g.close()
    print('finished!')