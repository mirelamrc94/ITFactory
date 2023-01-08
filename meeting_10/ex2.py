import math
import functools
import time
import random

#un decorator este si el in sine tot o functie, o fucntie care lucreaza cu o functie
# chronometer - decorator
#my_function -  o functie oarecare pe care dorim sa o cronometram

def chronometer(my_function):
    @functools.wraps(my_function) # cronometrul va 'imbraca' my_function
    def wrapper(*args, **kwargs): # *args **kwargs acopera orice argumente ar putea avea o functie oarecare my_function
        t1 = time.time() # luam timpul din sistem dianinte de a chema my_function
        result = my_function(*args, **kwargs) # invocam functia my_function
        t2 = time.time() # timpul din sistem dupa functia my_function
        duration = t2 - t1
        print(f"Functia {my_function.__name__} a durat {duration} secunde")
        return result # returnam rezultatul functiei my_function
    return wrapper

@chronometer
def sin_map(x_list):  #sinusul unui nr este intre -1 si 1
    y_list = []
    for x in x_list:
        y = (math.sin(x) + math.cos(x)) * math.pi
        y_list.append(y)
    return y_list

if __name__ == "__main__":

    l = [0, 1, 1.6, 2 ,3 ,4]

    my_list = []
    for i in range(1000):
        x = random.randint(0,100) # generez un nr x cuprins inte 0 si 100
        my_list.append(x)

  #  print(sin_map(l))
    y1 = sin_map(l)
    print("==============")
   # print(sin_map(my_list))
    y2 = sin_map(my_list)
