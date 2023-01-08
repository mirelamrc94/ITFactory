
class Monitor:

    def __init__(self, size = "50cm", resolution = "1920x740"):
        self.size = size
        self.resolution = resolution

class Tastatura:
    def __init__(self, keyboardtype = "qwerty"):
        self.keyboardtype = keyboardtype

class Switch:
    def __init__(self, state = "off"):
        self.state = state

class PowerButton:
    # va tine evidenta daca clasa a mai instantiat vreun obiect sau nu
    __instance = None

    def __init__(self, color = "red"):
        self.color = color
        self.state = "off"

    def __new__(cls, *args):
        print("PowerBotton.__new__()")
        # daca pana in momentul acesta nu a fost instantiat nici un obiect de tip powerbuton
        if cls.__instance is None:
        # atunci alocam un obiect de tip powerbutton si tinem eviddenta lui cls.__instantce
            cls.__instance = object.__new__(cls)
            #returnam adresa obiectului de tip powerbutton indiferent daca a fost alocat acum sau la un apel __new__ anterior
        return cls.__instance


    def toggle(self):
        if self.state == "off":
            self.state = "on"
        else:
            self.state = "off"


if __name__ == '__main__':
    print('hello world')

    m1 = Monitor()
    m2 = Monitor()
    t1 = Tastatura()
    t2 = Tastatura()

    s1 = Switch()
    s2 = Switch()

    print(type(m1))
    print(type(m2))

    print(id(m1))
    print(id(m2))
    print('`==================================')
    print(type(t1))
    print(type(t2))

    print(id(t1))
    print(id(t2))
    print('`==================================')
    print(type(s1))
    print(type(s2))

    print(id(s1))
    print(id(s2))
    print('`==================================')

    b1 = PowerButton()
    print(type(b1))
    print(id(b1))

    b2 = PowerButton()
    print(type(b2))
    print(id(b2))
    b3 = PowerButton()

    print(f"b1 state before toggle : {b1.state}")
    b2.toggle()
    print(f"b1 state after toggle : {b1.state}")
    b3.toggle()
    print(f"b1 state before toggle : {b1.state}")

