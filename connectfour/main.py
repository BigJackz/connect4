import pygame
import sys
from logiikka import voiton_tarkastaja
from logiikka import vuoro

YELLOW = (253,253,77)
PAAVALIKKO_POS = (450,30)

class peli:
    def __init__(self) -> None:
        #pelin alustamiseen tarkoitetut muuttujat
        pygame.init()
        self.pelaajan_vuoro = vuoro()
        self.tilanne = 2
        self.voittaja = 0
        self.voitto = False
        self.pelipoyta = [
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

        #Täällä peli pysyy hengissä :)
        self.silmukka()

    #Tyhjentää pöydän
    def tyhjenna_poyta(self):
        self.pelipoyta = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
        ]


    # tarkistetaan onko jonpi kumpi pelaajista voittanut
    def voiton_tarkastaja(self):
        v = voiton_tarkastaja()
        tieto = v.voitto_vaakasuunnassa(self.pelipoyta)
        tieto2 = v.voitto_pystysuunnassa(self.pelipoyta)
        tieto3 = v.voitto_diagonaalissa(self.pelipoyta)
        #Print komennot debuggausta varten poistuu viimeistään viimeisessä versiossa
        for i in range(6):
            print(self.pelipoyta[i])
        print("mogus")
        #tietox[0] kertoo onko onko voitto saavutettu jos on arvona boolean True, muutoin False
        #tietox[1] kertoo kumpi pelaajista on kyseessä saa arvon int joka on aluksi 0 ja vaihtuu joko arvoon 1 tai 2
        #self.voitto kertoo onko peliä voitettu. Tämä hävittää mahdollisuuden jatkaa pelin pelaamista sen jälkeen kun jompi kumpi pelaajista on saavuttanut voiton
        if tieto[0]:
            self.voittaja = tieto[1]
            print(f"Pelaaja {tieto[1]} voitti! (vaakasuunnassa)")
            self.voitto = True

        elif tieto2[0]:
            self.voittaja = tieto2[1]
            print(f"Pelaaja {tieto2[1]} voitti! (pystysuunnassa)")
            self.voitto = True

        elif tieto3[0]:
            self.voittaja = tieto3[1]
            print(f"Pelaaja {tieto3[1]} voitti! (diagonaalissa)")
            self.voitto = True

    #Tällä metodilla asetetaan pala oikeaan kohtaan ja vaihdetaan pelaajan vuoroa
    def aseta_pala(self, koordinaatti):
        for i in range(5,-1,-1):
            if self.pelipoyta[i][koordinaatti] == 0:
                self.pelipoyta[i][koordinaatti] = self.pelaajan_vuoro.get_vuoro() #asetetaan self.pelaajaa vastaava laatta paikoilleen
                break
        else:
            self.pelaajan_vuoro.vaihda_vuoro()
        self.voiton_tarkastaja()


    #pelipöydän päivittämiseen käytetty metodi
    def paivita_pelipoyta(self, x_koordinaatti):
        x = str(x_koordinaatti)
        aito_x = int(x[0])
        if len(x) < 3: #jos x alle 3 mittainen kyseessä ensimmäinen sarake
            self.aseta_pala(0)
            #print(0)
        else:
            self.aseta_pala(aito_x)
            #print(aito_x)

    #Pelisiirto tarkistaa koordinaateista mihinkä kohtaan pelaaja on asettamassa laattaa ja asettaa sen siihen kohtaan x koordinaatteja 
    def pelisiirto(self, koordinaatit):
        if koordinaatit[0] > 80 and koordinaatit[0] < 680:
            self.paivita_pelipoyta(koordinaatit[0])
        if koordinaatit[0] <= 80:
            self.paivita_pelipoyta(koordinaatit[0])
        self.pelaajan_vuoro.vaihda_vuoro()
        #print(koordinaatit)

    #tutkii jatkuvasti onko pelissä tapahtunut jotakin, jos on tehdään siihen liittyvät toimenpiteet
    def tutki_tapahtuma(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                if tapahtuma.button == 1:
                    if self.voitto:
                        self.tilanne = 3
                        self.napit(tapahtuma.pos)
                    if self.tilanne == 1:
                        self.napit(tapahtuma.pos)
                        self.pelisiirto(tapahtuma.pos)
                    elif self.tilanne == 2:
                        self.napit(tapahtuma.pos)
                        print(tapahtuma.pos)

    #pelissä olevien nappien luonti
    def napit(self, koordinaatit):
        if koordinaatit[0] > self.naytto.get_width()/7 and koordinaatit[0] < self.naytto.get_width()/7+150 and koordinaatit[1] > self.naytto.get_height()/7 and koordinaatit[1] < self.naytto.get_height()/7+50:
            print("kek")
            self.tyhjenna_poyta()
            self.tilanne = 1
            self.pelaajan_vuoro.set_vuoro(1)
        if koordinaatit[0] > 450 and koordinaatit[0] < 650 and koordinaatit[1] > 30 and koordinaatit[1] < 80:
            self.tilanne = 2
            self.voitto = False
        pass

    #Pelin elossa pitävä silmukka
    def silmukka(self):
        while True:
            self.tutki_tapahtuma()
            self.piirra_naytto()

    #Ladataan pelissä käytettävät kuvat
    def lataa_kuvat(self):
        self.kuvat = []
        for kuva in ["tyhja", "ismo", "seppo"]:
            self.kuvat.append(pygame.image.load(kuva + ".png"))

    #Näytön päivittämiseen käytettävä metodi
    def piirra_naytto(self):
        impact = pygame.font.SysFont('impact', 50)
        impact_35 = pygame.font.SysFont('impact', 35)
        palaa = impact_35.render('Päävalikkoon', True, (YELLOW))
        if self.voitto:
            vuoro = impact.render(f'Pelaaja {self.voittaja} voitti!', True, YELLOW)
        elif self.tilanne == 1:
            vuoro = impact.render(f'Pelaajan {self.pelaajan_vuoro.get_vuoro()} vuoro!', True, YELLOW)

        if self.tilanne == 1:
            self.naytto.fill((20, 60, 200))
            for y in range(6):
                for x in range(7):
                    ruutu = self.pelipoyta[y][x]
                    self.naytto.blit(self.kuvat[ruutu], (x * 100, y*100+100))
                    self.naytto.blit(vuoro, (10,20))
                    self.naytto.blit(palaa, (450,30))

                    
            pygame.display.flip()
        
        elif self.tilanne == 2:
            self.naytto.fill((255,255,255))
            s = pygame.font.SysFont('Impact',30)
            pelaa = s.render('Pelaa', True, (0,0,0))
            poistu = s.render('Poistu', True, (0,0,0))
            pygame.draw.rect(self.naytto, (0,200,30), (self.naytto.get_width()/7,self.naytto.get_height()/7,150,50))
            
            pygame.draw.rect(self.naytto,(0,200,30), (self.naytto.get_width()/7,self.naytto.get_height()/2 - 200,150,50))
            
            self.naytto.blit(pelaa, (105,115))
            self.naytto.blit(poistu, (105,315))
            pygame.display.flip()


peli()