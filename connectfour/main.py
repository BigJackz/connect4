import pygame
import sys
from logiikka import VoitonTarkastaja
from logiikka import Vuoro
import random
import math
from minimax import Minimax

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (20, 60, 200)
YELLOW = (253,253,77)
MENU = 2
PELI = 1
VOITTO = 3
AI_VAIKEUSASTEEN_VALINTA = 4
NOVIISI = 1
ENNENKI = 3
MESTARI = 6



class peli:
    def __init__(self) -> None:
        #pelin alustamiseen tarkoitetut muuttujat
        pygame.init()
        self.impact = pygame.font.SysFont('Impact',50)
        self.AI_vuoro = False
        self.AI_peli = False
        self.pelaajan_vuoro = Vuoro()
        self.voiton_tarkistaja = VoitonTarkastaja()
        self.minmax = Minimax()
        self.vaikeusaste = NOVIISI
        self.tilanne = MENU
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
        tieto = self.voiton_tarkistaja.voitto_vaakasuunnassa(self.pelipoyta)
        tieto2 = self.voiton_tarkistaja.voitto_pystysuunnassa(self.pelipoyta)
        tieto3 = self.voiton_tarkistaja.voitto_diagonaalissa(self.pelipoyta)
        #Print komennot debuggausta varten poistuu viimeistään viimeisessä versiossa
        #for i in range(6):
        #    print(self.pelipoyta[i])
        
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
    def aseta_pala(self, sarake):
        for i in range(5,-1,-1):
            if self.pelipoyta[i][sarake] == 0:
                self.pelipoyta[i][sarake] = self.pelaajan_vuoro.get_vuoro() #asetetaan self.pelaajaa vastaava laatta paikoilleen
                break
        else:
            self.pelaajan_vuoro.vaihda_vuoro()
        self.voiton_tarkastaja()

    #pygamen koordinaateista muunto yhdeksi int arvoksi joka merkkaa saraketta
    def sarake_koordinaateista(self, koordinaatit):
        x_koordinaatti = koordinaatit[0]
        print(x_koordinaatti)
        x = str(x_koordinaatti)
        uusi_x = x[0]
        sarake = int(uusi_x)
        if len(x) < 3:
            return 0
        else:
            return sarake

    #Pelisiirto tarkistaa koordinaateista mihinkä kohtaan pelaaja on asettamassa laattaa ja asettaa sen siihen kohtaan x koordinaatteja 
    def pelisiirto(self, sarake):
        #sarake = self.sarake_koordinaateista(koordinaatit)
        if self.voi_asettaa(sarake, self.pelipoyta):
            self.aseta_pala(sarake)
            self.pelaajan_vuoro.vaihda_vuoro()
            if self.AI_peli:
                self.AI_vuoro = True
        #print(koordinaatit)

    #tutkii jatkuvasti onko pelissä tapahtunut jotakin, jos on tehdään siihen liittyvät toimenpiteet
    def tutki_tapahtuma(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:

                if tapahtuma.button == 1:
                    if self.voitto:
                        self.tilanne = VOITTO
                        self.napit(tapahtuma.pos)
                    if self.tilanne == PELI:
                        self.napit(tapahtuma.pos)
                        sarake = self.sarake_koordinaateista(tapahtuma.pos)
                        self.pelisiirto(sarake)
                    if self.tilanne == MENU:
                        self.napit(tapahtuma.pos)
                        print(tapahtuma.pos)
                    elif self.tilanne == AI_VAIKEUSASTEEN_VALINTA:
                        self.vaikeusaste_napit(tapahtuma.pos)
                        print(tapahtuma.pos)
                    
                    

    #pelissä olevien nappien luonti
    def napit(self, koordinaatit):
        #nappi jolla aloitetaan 1vs1 peli
        if koordinaatit[0] > 105 and koordinaatit[0] < 220 and koordinaatit[1] > 120 and koordinaatit[1] < 166 and self.tilanne == MENU:
            self.voitto = False
            self.AI_peli = False
            self.tyhjenna_poyta()
            self.tilanne = PELI
            self.pelaajan_vuoro.set_vuoro(1)
        #nappi joka vie takaisin päävalikkoon
        if koordinaatit[0] > 450 and koordinaatit[0] < 650 and koordinaatit[1] > 30 and koordinaatit[1] < 80:
            self.tilanne = MENU
            self.voitto = False
            self.AI_peli = False
            self.pelaajan_vuoro.set_vuoro(1)
            self.tyhjenna_poyta()
        #nappi jolla aloitetaan peli ai:n kanssa
        if koordinaatit[0] > 90 and koordinaatit[0] < 550 and koordinaatit[1] > 300 and koordinaatit[1] < 366 and self.tilanne == MENU:
            self.tilanne = AI_VAIKEUSASTEEN_VALINTA
            #pygame.time.wait(500)

        #nappi jolla poistutaan pelistä
        if koordinaatit[0] > 105 and koordinaatit[0] < 235 and koordinaatit[1] > 520 and koordinaatit[1] < 566 and self.tilanne == MENU:
            quit()

    def vaikeusaste_napit(self, koordinaatit):
        #noviisi asettaa minimax syvyyden arvoon 1
        if koordinaatit[0] > 105 and koordinaatit[0] < 244 and koordinaatit[1] > 120 and koordinaatit[1] < 166:
            self.vaikeusaste = NOVIISI
            self.pelin_alustaminen_ai_vastaan()
        #Ennenki pelannu asettaa minimax syvyyden arvoon 3
        if koordinaatit[0] > 90 and koordinaatit[0] < 444 and koordinaatit[1] > 300 and koordinaatit[1] < 365:
            self.vaikeusaste = ENNENKI
            self.pelin_alustaminen_ai_vastaan()
        #Mestari asettaa minimax syvyyden arvoon 6
        if koordinaatit[0] > 105 and koordinaatit[0] < 262 and koordinaatit[1] > 520 and koordinaatit[1] < 566:
            self.vaikeusaste = MESTARI
            self.pelin_alustaminen_ai_vastaan()

    #Alustaa pelin AI:ta vastaan
    def pelin_alustaminen_ai_vastaan(self):
        self.pelaajan_vuoro.set_vuoro(1)
        self.voitto = False
        self.tyhjenna_poyta()
        self.tilanne = PELI
        self.AI_peli = True

    #tarkistaa onko ylimmällä rivillä kyseisellä sarakkellaa 0 jos on niin sinne voi vielä asettaa laatan
    def voi_asettaa(self, sarake, taulukko):
        if taulukko[0][sarake] == 0:
            return True
        else:
            return False

    #AI:n peliliikkeen toteuttaminen
    def AI_peliliike(self):
        paras_kohta, pisteet = self.minmax.minimax(self.pelipoyta, self.vaikeusaste, -math.inf, math.inf, True)
        if self.voi_asettaa(paras_kohta, self.pelipoyta):
            self.pelisiirto(paras_kohta)
            self.AI_vuoro = False

    #Pelin elossa pitävä silmukka
    def silmukka(self):
        while True:
            if self.AI_vuoro and self.AI_peli and not self.voitto and self.pelaajan_vuoro.get_vuoro() == 2:
                self.AI_peliliike()
            else:
                self.tutki_tapahtuma()
            self.piirra_naytto()

    #Ladataan pelissä käytettävät kuvat
    def lataa_kuvat(self):
        self.kuvat = []
        for kuva in ["tyhja", "ismo", "seppo"]:
            self.kuvat.append(pygame.image.load(kuva + ".png"))

    #Näytön päivittämiseen käytettävä metodi
    def piirra_naytto(self):
        self.piirra_pelitilanne()
        if self.tilanne == MENU:
            self.piirra_menu()
        if self.tilanne == AI_VAIKEUSASTEEN_VALINTA:
            self.piirra_sepon_vaikeusasteet_menu()
    
    def piirra_pelitilanne(self):
        impact_35 = pygame.font.SysFont('impact', 35)
        palaa = impact_35.render('Päävalikkoon', True, (YELLOW))
        if self.voitto:
            if self.AI_peli and self.voittaja == 2:
                vuoro = self.impact.render(f"Seppo voitti!", True, YELLOW)
            elif self.AI_peli and self.voittaja == 1:
                vuoro = self.impact.render(f"Voitit Sepon!", True, YELLOW)
            else:
                vuoro = self.impact.render(f'Pelaaja {self.voittaja} voitti!', True, YELLOW)
        elif self.tilanne == PELI:
            vuoro = self.impact.render(f'Pelaajan {self.pelaajan_vuoro.get_vuoro()} vuoro!', True, YELLOW)

        if self.tilanne == PELI:
            self.naytto.fill(BLUE)
            for y in range(6):
                for x in range(7):
                    ruutu = self.pelipoyta[y][x]
                    self.naytto.blit(self.kuvat[ruutu], (x * 100, y*100+100))
                    self.naytto.blit(vuoro, (10,20))
                    self.naytto.blit(palaa, (450,30))
            pygame.display.flip()

    #Käytetään sepon vaikeusaste menun piirtämiseen
    def piirra_sepon_vaikeusasteet_menu(self):
        self.naytto.fill(WHITE)
        taso1 = self.impact.render('Noviisi', True, BLACK)
        taso2 = self.impact.render('Ennenki pelannu', True, BLACK)
        taso3 = self.impact.render('Mestari', True, BLACK)
        self.naytto.blit(taso1, (105,115))
        self.naytto.blit(taso2, (105,315))
        self.naytto.blit(taso3, (105,515))
        pygame.display.flip()

    #Käytetään menun piirtämiseen
    def piirra_menu(self):
        self.naytto.fill(WHITE)
        pelaa = self.impact.render('Pelaa', True, BLACK)
        poistu = self.impact.render('Poistu', True, BLACK)
        ai_peli = self.impact.render('Pelaa Seppoa vastaan', True, BLACK)
        self.naytto.blit(pelaa, (105,115))
        self.naytto.blit(poistu, (105,515))
        self.naytto.blit(ai_peli, (105,315))
        pygame.display.flip()


peli()