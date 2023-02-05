

class voiton_tarkastaja():
    def __init__(self) -> None:
        pass

    #Tarkistaa onko voittoa saavutettu diagonaalissa
    def voitto_diagonaalissa(self, taulukko):
        for i in range(7):
            laskuri_1 = 0
            laskuri_2 = 0
            if taulukko[3][i] != 0:   #tarkistetaan onko neljännellä rivillä muuta arvoa kuin 0 jos ei, niin ei ole mahdollista voittaa diagonaalissa
                luku = i-3
                if luku < 0:
                    luku = abs(luku)
                    for ii in range(7-luku):
                        if taulukko[luku+ii][0+ii] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        elif taulukko[luku+ii][0+ii] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        elif taulukko[luku+ii][0+ii] == 2:
                            laskuri_2 += 1
                            laskuri_1 = 0
                            if laskuri_2 == 4:
                                return True,2

                else:
                    for ii in range(7-luku):
                        if taulukko[0+ii][luku+ii] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        if taulukko[0+ii][luku+ii] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        if taulukko[0+ii][luku+ii] == 2:
                            laskuri_2 += 1
                            laskuri_1 = 0
                            if laskuri_2 == 4:
                                return True,2
                
                luku2 = i-3
                if luku2 <= 0:
                    luku = abs(luku)
                    for ii in range(7-luku):
                        if taulukko[0+ii][6-luku-ii] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        if taulukko[0+ii][6-luku-ii] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        if taulukko[0+ii][6-luku-ii] == 2:
                            laskuri_1 = 0
                            laskuri_2 += 1
                            if laskuri_2 == 4:
                                return True,2
                else:
                    for ii in range(7-luku):
                        if taulukko[luku+ii][6-ii] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        if taulukko[luku+ii][6-ii] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        if taulukko[luku+ii][6-ii] == 2:
                            laskuri_1 = 0
                            laskuri_2 += 1
                            if laskuri_2 == 4:
                                return True,2
        else:
            return False,0
        
    #Tarkistetaan onko voittoa saavutettu vaakasuunnassa, jos voitto löytyi palautetaan 
    #Tuple True,(pelaajan numero), jos ei löytynyt niin palautetaan Tuple (False,0)
    def voitto_vaakasuunnassa(self, taulukko):
        for y in range(len(taulukko)):
            jonossa_1 = 0
            jonossa_2 = 0
            for x in taulukko[y]:
                if x == 0:
                    jonossa_1 = 0
                    jonossa_2 = 0
                if x == 1:
                    jonossa_1 += 1
                    jonossa_2 = 0
                elif x == 2:
                    jonossa_2 += 1
                    jonossa_1 = 0
                if jonossa_1 == 4:
                    print("pelaaja 1 on viineri")
                    return True,1
                if jonossa_2 == 4:
                    print("pelaaja 2 on viineri")
                    return True,2
        return False,0

    def voitto_pystysuunnassa(self, taulukko):

        for i in range(4):           # Käydään läpi pelipöydän 4 ylintä tasoa, koska vasta 4 rivillä voi olla 4 pystysuunnassa olevaa laattaa          
            for ii in range(7):
                laatta = taulukko[i][ii]
                laskuri_1 = 0           # pidetään täällä tieto siitä onko 4 samaa laattaa pystysuunnassa pelaajalla 1
                laskuri_2 = 0           # pidetään täällä tieto siitä onko 4 samaa laattaa pystysuunnassa pelaajalla 2
                if laatta == 1:
                    for y in range(4):
                        if taulukko[i+y][ii] == 1:
                            laskuri_1 += 1
                            if laskuri_1 == 4:
                                print("player 1 is the viiner")
                                return True,1
                        else:
                            break
                elif laatta == 2:
                    for y in range(4):
                        if taulukko[i+y][ii] == 2:
                            laskuri_2 += 1
                            if laskuri_2 == 4:
                                print("player 2 is the viiner")
                                return True,2
                        else:
                            break
        else:                
            return False,0
        
#vuoroa käsittelevä luokka
class vuoro():
    def __init__(self) -> None:
        self.vuoro = 1

    def get_vuoro(self):
        return self.vuoro
    
    def set_vuoro(self, vuoro):
        self.vuoro = vuoro
    
    def vaihda_vuoro(self):
        if self.vuoro == 1:
            self.vuoro = 2
        elif self.vuoro == 2:
            self.vuoro = 1

    # Tällä vaihdetaan kumman pelaajan vuoro on asettaa laatta
    def vaihda_vuoro(self):
        if self.vuoro == 1:
            self.vuoro = 2
        elif self.vuoro == 2:
            self.vuoro = 1