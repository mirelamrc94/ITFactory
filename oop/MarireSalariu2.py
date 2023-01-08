
from oop.MarireSalariu import Angajat

angajat1 = Angajat('State', 'Vasile', 2000, 3, 'tractorist')
angajat2 = Angajat('Stamate', 'Ioana', 2300, 5, 'mecanic')

angajat1.DescriereAngajat()
angajat2.DescriereAngajat()

angajat1.MarireSalariu()
angajat2.MarireSalariu()

angajat1.ActualizareVechime(2)
angajat2.ActualizareVechime(1)


angajat1.MarireSalariu()
angajat2.MarireSalariu()
