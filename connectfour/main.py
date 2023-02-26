import pygame
from peli_logiikka import Peli

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


class UI:
    def __init__(self) -> None:
        #pelin alustamiseen tarkoitetut muuttujat
        pygame.init()
        self.peli = Peli()
        self.impact = pygame.font.SysFont('Impact',50)
        self.korkeus = 680
        self.leveys = 680
        self.lataa_kuvat()
        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus))
        pygame.display.set_caption("Connect4")

        #Täällä peli pysyy hengissä :)
        self.silmukka()


    #tutkii jatkuvasti onko pelissä tapahtunut jotakin, jos on tehdään siihen liittyvät toimenpiteet
    def tutki_tapahtuma(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:

                if tapahtuma.button == 1:
                    if self.peli.palauta_onko_voittoa():
                        self.peli.aseta_tilanne(VOITTO)
                        self.napit(tapahtuma.pos)
                        
                    if self.peli.palauta_tilanne() == PELI:
                        self.napit(tapahtuma.pos)
                        sarake = self.peli.sarake_koordinaateista(tapahtuma.pos)
                        self.peli.pelisiirto(sarake)

                    if self.peli.palauta_tilanne() == MENU:
                        self.napit(tapahtuma.pos)
                        print(tapahtuma.pos)

                    elif self.peli.palauta_tilanne() == AI_VAIKEUSASTEEN_VALINTA:
                        self.vaikeusaste_napit(tapahtuma.pos)
                        print(tapahtuma.pos)
                    
                    

    #pelissä olevien nappien luonti
    def napit(self, koordinaatit):
        #nappi jolla aloitetaan 1vs1 peli
        if koordinaatit[0] > 105 and koordinaatit[0] < 220 and koordinaatit[1] > 120 and koordinaatit[1] < 166 and self.peli.palauta_tilanne() == MENU:
            self.peli.aloita_1v1_peli()

        #nappi joka vie takaisin päävalikkoon
        if koordinaatit[0] > 450 and koordinaatit[0] < 650 and koordinaatit[1] > 30 and koordinaatit[1] < 80:
            self.peli.paavalikkoon()

        #nappi jolla aloitetaan peli ai:n kanssa
        if koordinaatit[0] > 90 and koordinaatit[0] < 550 and koordinaatit[1] > 300 and koordinaatit[1] < 366 and self.peli.palauta_tilanne() == MENU:
            self.peli.ai_peli()
            #pygame.time.wait(500)

        #nappi jolla poistutaan pelistä
        if koordinaatit[0] > 105 and koordinaatit[0] < 235 and koordinaatit[1] > 520 and koordinaatit[1] < 566 and self.peli.palauta_tilanne() == MENU:
            quit()

    def vaikeusaste_napit(self, koordinaatit):
        #noviisi asettaa minimax syvyyden arvoon 1
        if koordinaatit[0] > 105 and koordinaatit[0] < 244 and koordinaatit[1] > 120 and koordinaatit[1] < 166:
            self.peli.vaihda_ai_vaikeustaso(NOVIISI)
            self.peli.pelin_alustaminen_ai_vastaan()

        #Ennenki pelannu asettaa minimax syvyyden arvoon 3
        if koordinaatit[0] > 90 and koordinaatit[0] < 444 and koordinaatit[1] > 300 and koordinaatit[1] < 365:
            self.peli.vaihda_ai_vaikeustaso(ENNENKI)
            self.peli.pelin_alustaminen_ai_vastaan()

        #Mestari asettaa minimax syvyyden arvoon 6
        if koordinaatit[0] > 105 and koordinaatit[0] < 262 and koordinaatit[1] > 520 and koordinaatit[1] < 566:
            self.peli.vaihda_ai_vaikeustaso(MESTARI)
            self.peli.pelin_alustaminen_ai_vastaan()

    #Pelin elossa pitävä silmukka
    def silmukka(self):
        while True:
            if self.peli.onko_ai_vuoro() and self.peli.onko_ai_peli() and not self.peli.palauta_onko_voittoa() and self.peli.vuoro.get_vuoro() == 2:
                self.peli.AI_peliliike()
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
        if self.peli.palauta_tilanne() == MENU:
            self.piirra_menu()
        if self.peli.palauta_tilanne() == AI_VAIKEUSASTEEN_VALINTA:
            self.piirra_sepon_vaikeusasteet_menu()
    
    def piirra_pelitilanne(self):
        impact_35 = pygame.font.SysFont('impact', 35)
        palaa = impact_35.render('Päävalikkoon', True, (YELLOW))
        if self.peli.palauta_onko_voittoa():
            if self.peli.onko_ai_peli() and self.peli.palauta_voittaja() == 2:
                vuoro = self.impact.render(f"Seppo voitti!", True, YELLOW)
            elif self.peli.onko_ai_peli() and self.peli.palauta_voittaja() == 1:
                vuoro = self.impact.render(f"Voitit Sepon!", True, YELLOW)
            else:
                vuoro = self.impact.render(f'Pelaaja {self.peli.palauta_voittaja()} voitti!', True, YELLOW)
        elif self.peli.palauta_tilanne() == PELI:
            vuoro = self.impact.render(f'Pelaajan {self.peli.vuoro.get_vuoro()} vuoro!', True, YELLOW)

        if self.peli.palauta_tilanne() == PELI:
            self.naytto.fill(BLUE)
            for y in range(6):
                for x in range(7):
                    ruutu = self.peli.get_poyta()[y][x]

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


UI()