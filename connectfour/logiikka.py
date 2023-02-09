

class voiton_tarkastaja():
    def __init__(self) -> None:
        pass

    #Tarkistaa onko voittoa saavutettu diagonaalissa
    def voitto_diagonaalissa(self, taulukko):
        for x in range(7):
            if taulukko[2][x] != 0: #tarkistetaan onko kolmannella rivillä muuta arvoa kuin 0 jos ei, niin ei ole mahdollista voittaa diagonaalissa
                laskuri_1 = 0
                laskuri_2 = 0
                luku = 2 - x
                luku2 = 2 + x
                if luku == 0:
                    for i in range(6):
                        if taulukko[i][i] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        if taulukko[i][i] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        if taulukko[i][i] == 2:
                            laskuri_2 += 1
                            laskuri_1 = 0
                            if laskuri_2 == 4:
                                return True,2
                if luku > 0:
                    for i in range(6-luku):
                        if taulukko[luku+i][i] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        if taulukko[luku+i][i] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        if taulukko[luku+i][i] == 2:
                            laskuri_2 += 1
                            laskuri_1 = 0
                            if laskuri_2 == 4:
                                return True,2
                if luku < 0:
                    luku = abs(luku)
                    for i in range(7-luku):
                        if taulukko[i][luku+i] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        if taulukko[i][luku+i] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        if taulukko[i][luku+i] == 2:
                            laskuri_2 += 1
                            laskuri_1 = 0
                            if laskuri_2 == 4:
                                return True,2
                if luku2 == 6:
                    for i in range(6):
                        if taulukko[i][luku2-i] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        if taulukko[i][luku2-i] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        if taulukko[i][luku2-i] == 2:
                            laskuri_2 += 1
                            laskuri_1 = 0
                            if laskuri_2 == 4:
                                return True,2
                if luku2 > 6:
                    luku2 = luku2 - 6
                    for i in range(6-luku2):
                        if taulukko[luku2+i][6-i] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        if taulukko[luku2+i][6-i] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        if taulukko[luku2+i][6-i] == 2:
                            laskuri_2 += 1
                            laskuri_1 = 0
                            if laskuri_2 == 4:
                                return True,2
                if luku2 < 6:
                    for i in range(luku2+1):
                        if taulukko[i][luku2-i] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        if taulukko[i][luku2-i] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        if taulukko[i][luku2-i] == 2:
                            laskuri_2 += 1
                            laskuri_1 = 0
                            if laskuri_2 == 4:
                                return True,2
                    
        return False,0
                        
                        
    #    for i in range(6):
    #        laskuri_1 = 0
    #        laskuri_2 = 0
    #        if taulukko[3][i] != 0:   #tarkistetaan onko neljännellä rivillä muuta arvoa kuin 0 jos ei, niin ei ole mahdollista voittaa diagonaalissa
    #            luku = i-3
    #            if luku < 0:
    #                luku = abs(luku)
    #                for ii in range(6-luku):
    #                    if taulukko[luku+ii][0+ii] == 0:
    #                        laskuri_1 = 0
    #                        laskuri_2 = 0
    #                    elif taulukko[luku+ii][0+ii] == 1:
    #                        laskuri_1 += 1
    #                        laskuri_2 = 0
    #                        if laskuri_1 == 4:
    #                            return True,1
    #                    elif taulukko[luku+ii][0+ii] == 2:
    #                        laskuri_2 += 1
    #                        laskuri_1 = 0
    #                        if laskuri_2 == 4:
    #                            return True,2
#
    #            else:
    #                for ii in range(6-luku):
    #                    if taulukko[0+ii][luku+ii] == 0:
    #                        laskuri_1 = 0
    #                        laskuri_2 = 0
    #                    if taulukko[0+ii][luku+ii] == 1:
    #                        laskuri_1 += 1
    #                        laskuri_2 = 0
    #                        if laskuri_1 == 4:
    #                            return True,1
    #                    if taulukko[0+ii][luku+ii] == 2:
    #                        laskuri_2 += 1
    #                        laskuri_1 = 0
    #                        if laskuri_2 == 4:
    #                            return True,2
    #            laskuri_1 = 0
    #            laskuri_2 = 0
    #            luku2 = i-3
    #            if luku2 <= 0:
    #                luku = abs(luku)
    #                for ii in range(6-luku):
    #                    if taulukko[0+ii][6-luku-ii] == 0:
    #                        laskuri_1 = 0
    #                        laskuri_2 = 0
    #                    if taulukko[0+ii][6-luku-ii] == 1:
    #                        laskuri_1 += 1
    #                        laskuri_2 = 0
    #                        if laskuri_1 == 4:
    #                            return True,1
    #                    if taulukko[0+ii][6-luku-ii] == 2:
    #                        laskuri_1 = 0
    #                        laskuri_2 += 1
    #                        if laskuri_2 == 4:
    #                            return True,2
    #            else:
    #                for ii in range(6-luku):
    #                    if taulukko[luku+ii][6-ii] == 0:
    #                        laskuri_1 = 0
    #                        laskuri_2 = 0
    #                    if taulukko[luku+ii][6-ii] == 1:
    #                        laskuri_1 += 1
    #                        laskuri_2 = 0
    #                        if laskuri_1 == 4:
    #                            return True,1
    #                    if taulukko[luku+ii][6-ii] == 2:
    #                        laskuri_1 = 0
    #                        laskuri_2 += 1
    #                        if laskuri_2 == 4:
    #                            return True,2
    #    else:
    #        return False,0
        
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

    #Tarkistaa onko voittoa syntynyt pystysuunnassa kummallekaan pelaajalle
    def voitto_pystysuunnassa(self, taulukko):
        for i in range(7):
            if taulukko[2][i] != 0: # Käydään läpi kolmas rivi ylhäältä jos siellä sijaitsee jotain muuta kuin 0 niin on mahdollista että
                                    # että jommalla kummalla pelaajista on 4 pystysuunnassa peräkkäin
                laskuri_1 = 0       # Pitää yllä jos pelaaja 1 on saanut 4 pystysuunnassa peräkkäin
                laskuri_2 = 0       # Pitää yllä jos pelaaja 2 on saanut 4 pystysuunnassa peräkkäin
                for ii in range(6):
                    if taulukko[ii][i] == 0:
                        laskuri_2 = 0
                        laskuri_1 = 0
                    if taulukko[ii][i] == 1:
                        laskuri_1 += 1
                        laskuri_2 = 0
                    if taulukko[ii][i] == 2:
                        laskuri_2 += 1
                        laskuri_1 = 0
                    if laskuri_1 == 4:
                        return True,1
                    if laskuri_2 == 4:
                        return True,2
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