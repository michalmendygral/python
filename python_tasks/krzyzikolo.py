plansza = [i for i in range(1,10)]

def pokaz_plansze():
    for i in range(0,8,3):
        print(plansza[i],plansza[i+1],plansza[i+2])

#true krzyzyk ; false kolko
czyj_ruch=True
pokaz_plansze()

def wstaw(miejsce,znak):
    if plansza[miejsce] != "X" or plansza[miejsce] != "O":
        plansza[miejsce]=znak
        pokaz_plansze()
    else:
        print("Niedostepne!")

def reset():
    print("Wygarana ", "krzyzyk" if czyj_ruch == True else "kolko","\n\n")
    global plansza
    plansza = [i for i in range(1, 10)]
    print("_________")
    print("Nowa gra!")
    print("_________")
    pokaz_plansze()

def sprawdz():
    #poziom
    if plansza[0]==plansza[1] and plansza[1]==plansza[2] and plansza[0]!= "1":
        reset()
    elif plansza[3]==plansza[4] and plansza[4]==plansza[5] and plansza[4]!= "5":
        reset()
    elif plansza[6]==plansza[7] and plansza[7]==plansza[8] and plansza[7]!= "8":
        reset()
    #pion
    elif plansza[0] == plansza[3] and plansza[3] == plansza[6] and plansza[4] != "5":
        reset()
    elif plansza[1] == plansza[4] and plansza[4] == plansza[7] and plansza[4] != "1":
        reset()
    elif plansza[2]==plansza[5] and plansza[5]==plansza[8] and plansza[7]!= "8":
        reset()
    #skos
    elif plansza[0]==plansza[4] and plansza[4]==plansza[8] and plansza[8]!= "9":
        reset()
    elif plansza[2]==plansza[4] and plansza[4]==plansza[6] and plansza[6]!= "7":
        reset()

while True:
    print("Jestes ", "krzyzyk" if czyj_ruch==True else "kolko")
    miejsce = input("Podaj gdzie wstawic znak")
    znak = "X" if czyj_ruch==True else "O"
    wstaw(int(miejsce)-1,znak)
    sprawdz()
    czyj_ruch=not czyj_ruch
