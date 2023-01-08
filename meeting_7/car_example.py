class Car:

    def __init__(self, marca, model, culoare):
        #marcam atributele ca fiind private
        #prin __ ianinte de numele lor
        self.__marca = marca
        self.__model = model
        self.__culoare = culoare

    #getter pentru marca
    def get_marca(self):
        return self.__marca

    def get_model(self):
        return self.__model

    def get_culoare(self):
        return self.__culoare

    # setter pt culoare
    def set_culoare(self, culoare_noua):
        if culoare_noua in ['alb', 'negru']:
            print("nu putem schimba culoarea")
            return
        self.__culoare = culoare_noua

if __name__ == "__main__":

    c1 = Car ('vw', 'gold', 'galben')
    #c1.culoare = 'rosu'
    c1.set_culoare('albastru')
    c1.set_culoare('alb')


    print(c1.get_marca())
    print(c1.get_model())
    print(c1.get_culoare())