#uzywanie metod z ta sama nazwa w roznych klasach
class Ksztalt:
    def __init__(self,nazwa='Ksztalt'):
        self.nazwa = nazwa

    def pole(self):
        print('Brak danych na temat ', self.nazwa)

class Trojkat(Ksztalt):
    def __init__(self,nazwa='Trojkat', a =2, h=2):
        super().__init__(nazwa)
        self.a = a
        self.h = h

    def pole(self):
        print('Pole figury ', self.nazwa, ' = ' , self.a * self.h/2 , ' cm2')

class Prostokat(Ksztalt):
    def __init__(self,nazwa='Prostokat', a = 2, b =3):
        self.nazwa = nazwa
        self.a = a
        self.b = b

    def pole(self):
        print('Pole figury ', self.nazwa, ' = ' , self.a * self.b , ' cm2')

class Kwadrat(Ksztalt):
    def __init__(self,nazwa='Kwadrat', a = 2):
        self.nazwa = nazwa
        self.a = a

    def pole(self):
        print('Pole figury ', self.nazwa, ' = ' , self.a**2 , ' cm2')

ksztalt = Ksztalt()
trojkat = Trojkat()
prostokat = Prostokat()
kwadrat = Kwadrat()

for i in (ksztalt,trojkat,prostokat,kwadrat):
    i.pole()