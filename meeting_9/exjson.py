import json

if __name__ == "__main__":

    my_dict = {}
    my_dict["nume_carte"] = "Manual de programare"
    my_dict["an"] = 2021
    my_dict["autori"] = [ "Ionescu", "Popescu"]

    f = open("date_output.json", "w")
    #json.dump(my_dict, f)
    output = json.dumps(my_dict, indent=4)
    f.write(output)
    f.close()
