from tema6 import Cerc, Dreptunghi, Angajat, Cont


cerc1 = Cerc(4, "roz")
cerc2 = Cerc(20, 'negru')

cerc1.descriere_cerc()
cerc1.aria()
cerc1.diametru()
cerc1.circumferinta()
cerc1.descriere_cerc()
print('==================================')
dreptunghi1 = Dreptunghi(9, 5, 'mov')
dreptunghi1.descriere()
dreptunghi1.arie_dreptunghi()
dreptunghi1.perimetru_dreptunghi()
dreptunghi1.schimba_culoare('negru')
dreptunghi1.descriere()
print('==================================')

angajat1 = Angajat('Vasiliu', 'Daniel', 2000)
angajat1.descriere()
angajat1.nume_complet()
angajat1.salariu_lunar()
angajat1.salariu_anual()
angajat1.marire_salariu(25)
angajat1.salariu_lunar()
angajat1.salariu_anual()

print('======================================')

cont1 = Cont('RO22ABCRONCRT22541222000', "Alina Chersan", 1500)
cont1.afisare_sold()
cont1.debitare_cont(1200)
cont1.afisare_sold()
cont1.creditare_cont(3000)
cont1.afisare_sold()