

class BMW:

    def __init__(self, model, color, xdrive):
        self.model = model
        self.color = color
        self.xdrive = xdrive

    def drive(self):
        if self.xdrive:
            print(f'Driving BMW car model {self.model}, color {self.color}, with xdrive.')
        else:
            print(f'Driving BMW car model {self.model}, color {self.color}, without xdrive.')

class Audi:
    def __init__(self, model, color):
        self.model = model
        self.color = color


    def drive(self):
        print(f'Driving Audi car model {self.model}, color {self.color}.')

if __name__ == '__main__':

    c1 = BMW ('X1', 'Gray', True)
    c2 = Audi ('A4', 'Red')
    c3 = Audi ('Q5', 'White')

    cars_list = [c1, c2, c3]

    for car in cars_list:
        car.drive()
        print(type(car))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    # c1.drive()
    # c2.drive()
