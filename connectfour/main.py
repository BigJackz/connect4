import pygame


class peli:
    def __init__(self) -> None:
        self.pelaaja = 1
        self.pelipoyta = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
        ]
        self.korkeus = 680
        self.leveys = 680
        self.lataa_kuvat()

        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus))
        pygame.display.set_caption("Connect4")

        self.silmukka()


    # tarkistetaan onko jonpi kumpi pelaajista voittanut
    def voiton_tarkastaja(self):
        tieto = self.voitto_vaakasuunnassa()
        tieto2 = self.voitto_pystysuunnassa()
        tieto3 = self.voitto_diagonaalissa()
        for i in range(7):
            print(self.pelipoyta[i])
        if tieto[0]:
            print(f"Pelaaja {tieto[1]} voitti! (vaakasuunnassa)")
        if tieto2[0]:
            print(f"Pelaaja {tieto2[1]} voitti! (pystysuunnassa)")
        if tieto3[0]:
            print(f"Pelaaja {tieto3[1]} voitti! (diagonaalissa)")
        #self.voitto_diagonaalissa()
        

    #Tarkistaa onko voittoa saavutettu diagonaalissa
    def voitto_diagonaalissa(self):
        for i in range(7):
            laskuri_1 = 0
            laskuri_2 = 0
            if self.pelipoyta[3][i] != 0:   #tarkistetaan onko neljännellä rivillä muuta arvoa kuin 0 jos ei, niin ei ole mahdollista voittaa diagonaalissa
                luku = i-3
                
                if luku < 0:
                    luku = abs(luku)
                    for ii in range(7-luku):
                        if self.pelipoyta[luku+ii][0+ii] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        elif self.pelipoyta[luku+ii][0+ii] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        elif self.pelipoyta[luku+ii][0+ii] == 2:
                            laskuri_2 += 1
                            laskuri_1 = 0
                            if laskuri_2 == 4:
                                return True,2

                else:
                    for ii in range(7-luku):
                        if self.pelipoyta[0+ii][luku+ii] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        if self.pelipoyta[0+ii][luku+ii] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        if self.pelipoyta[0+ii][luku+ii] == 2:
                            laskuri_2 += 1
                            laskuri_1 = 0
                            if laskuri_2 == 4:
                                return True,2
                
                luku2 = i-3
                if luku2 <= 0:
                    luku = abs(luku)
                    for ii in range(7-luku):
                        if self.pelipoyta[0+ii][6-luku-ii] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        if self.pelipoyta[0+ii][6-luku-ii] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        if self.pelipoyta[0+ii][6-luku-ii] == 2:
                            laskuri_1 = 0
                            laskuri_2 += 1
                            if laskuri_2 == 4:
                                return True,2
                else:
                    for ii in range(7-luku):
                        if self.pelipoyta[luku+ii][6-ii] == 0:
                            laskuri_1 = 0
                            laskuri_2 = 0
                        if self.pelipoyta[luku+ii][6-ii] == 1:
                            laskuri_1 += 1
                            laskuri_2 = 0
                            if laskuri_1 == 4:
                                return True,1
                        if self.pelipoyta[luku+ii][6-ii] == 2:
                            laskuri_1 = 0
                            laskuri_2 += 1
                            if laskuri_2 == 4:
                                return True,2
        else:
            return False,0
            

    def voitto_pystysuunnassa(self): 
        for i in range(4):           # Käydään läpi pelipöydän 4 ylintä tasoa, koska vasta 4 rivillä voi olla 4 pystysuunnassa olevaa laattaa          
            for ii in range(7):
                laatta = self.pelipoyta[i][ii]
                laskuri_1 = 0           # pidetään täällä tieto siitä onko 4 samaa laattaa pystysuunnassa pelaajalla 1
                laskuri_2 = 0           # pidetään täällä tieto siitä onko 4 samaa laattaa pystysuunnassa pelaajalla 2
                if laatta == 1:
                    for y in range(4):
                        if self.pelipoyta[i+y][ii] == 1:
                            laskuri_1 += 1
                            if laskuri_1 == 4:
                                print("player 1 is the viiner")
                                return True,1
                        else:
                            break
                elif laatta == 2:
                    for y in range(4):
                        if self.pelipoyta[i+y][ii] == 2:
                            laskuri_2 += 1
                            if laskuri_2 == 4:
                                print("player 2 is the viiner")
                                return True,2
                        else:
                            break
        else:                
            return False,0


    #Tarkistetaan onko voittoa saavutettu vaakasuunnassa, jos voitto löytyi palautetaan Tuple True,(pelaajan numero), jos ei löytynyt niin palautetaan Tuple (False,0)
    def voitto_vaakasuunnassa(self):
        for y in range(len(self.pelipoyta)):
            jonossa_1 = 0
            jonossa_2 = 0
            for x in self.pelipoyta[y]:
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

    def aseta_pala(self, koordinaatti):
        for i in range(6,-1,-1):
            if self.pelipoyta[i][koordinaatti] == 0:
                self.pelipoyta[i][koordinaatti] = self.pelaaja #self.pelaaja #asetetaan self.pelaajaa vastaava laatta paikoilleen
                break
        else:
            self.vaihda_pelaajan_vuoro()
        self.voiton_tarkastaja()

        #paikka = 6
        #if self.pelipoyta[paikka][koordinaatti] == 0:
        #    self.pelipoyta[paikka][koordinaatti] = 
        #else:
        #    paikka -= 1
        #    self.pelipoyta[paikka][koordinaatti] = self.pelaaja

    def paivita_pelipoyta(self, x_koordinaatti):
        x = str(x_koordinaatti)
        aito_x = int(x[0])
        if len(x) < 3: #jos x alle 3 mittainen kyseessä ensimmäinen sarake
            self.aseta_pala(0)
            #print(0)
        else:
            self.aseta_pala(aito_x)
            #print(aito_x)


    # Tällä vaihdetaan kumman pelaajan vuoro on asettaa laatta
    def vaihda_pelaajan_vuoro(self):
        if self.pelaaja == 1:
            self.pelaaja = 2
        elif self.pelaaja == 2:
            self.pelaaja = 1


    def pelisiirto(self, koordinaatit):
        if koordinaatit[0] > 80 and koordinaatit[0] < 680:
            self.paivita_pelipoyta(koordinaatit[0])
        if koordinaatit[0] <= 80:
            self.paivita_pelipoyta(koordinaatit[0])
        self.vaihda_pelaajan_vuoro()
        #print(koordinaatit)


    def tutki_tapahtuma(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                if tapahtuma.button == 1:
                    self.pelisiirto(tapahtuma.pos)

    def silmukka(self):
        while True:
            self.tutki_tapahtuma()
            self.piirra_naytto()

    def lataa_kuvat(self):
        self.kuvat = []
        for kuva in ["tyhja", "ismo", "seppo"]:
            self.kuvat.append(pygame.image.load(kuva + ".png"))


    def piirra_naytto(self):
        self.naytto.fill((20, 60, 200))

        for y in range(7):
            for x in range(7):
                ruutu = self.pelipoyta[y][x]
                self.naytto.blit(self.kuvat[ruutu], (x * 100, y*100))
        pygame.display.flip()


peli()