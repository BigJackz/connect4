import pygame
import sys
from logiikka import voiton_tarkastaja
from logiikka import vuoro
import random
import math


YELLOW = (253,253,77)
PAAVALIKKO_POS = (450,30)
MENU = 2
PELI = 1
VOITTO = 3




class peli:
    def __init__(self) -> None:
        #pelin alustamiseen tarkoitetut muuttujat
        pygame.init()
        self.AI_vuoro = False
        self.AI_peli = False
        self.pelaajan_vuoro = vuoro()
        self.voiton_tarkistaja = voiton_tarkastaja()
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
                        print(self.loppu(self.pelipoyta))
                    elif self.tilanne == MENU:
                        self.napit(tapahtuma.pos)
                        print(tapahtuma.pos)

    #pelissä olevien nappien luonti
    def napit(self, koordinaatit):
        #nappi jolla aloitetaan 1vs1 peli
        if koordinaatit[0] > self.naytto.get_width()/7 and koordinaatit[0] < self.naytto.get_width()/7+150 and koordinaatit[1] > self.naytto.get_height()/7 and koordinaatit[1] < self.naytto.get_height()/7+50 and self.tilanne == MENU:
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
        if koordinaatit[0] > 90 and koordinaatit[0] < 400 and koordinaatit[1] > 300 and koordinaatit[1] < 350 and self.tilanne == MENU:
            self.pelaajan_vuoro.set_vuoro(1)
            self.voitto = False
            self.tyhjenna_poyta()
            self.tilanne = PELI
            self.AI_peli = True
            #self.pelaajan_vuoro.set_vuoro(random.randint(1,2))
        #nappi jolla poistutaan pelistä
        if koordinaatit[0] > 105 and koordinaatit[0] < 180 and koordinaatit[1] > 520 and koordinaatit[1] < 545 and self.tilanne == MENU:
            quit()
        pass

    #tarkistaa onko ylimmällä rivillä kyseisellä sarakkellaa 0 jos on niin sinne voi vielä asettaa laatan
    def voi_asettaa(self, sarake, taulukko):
        if taulukko[0][sarake] == 0:
            return True
        else:
            return False

    #annetaan pisteitä siitä kuinka hyvä pelitilanne on pelaajalle 2 eli AI:lle
    def pisteet_rivista(self, tarkastettava, laatta):
        pelaajan_laatta = 1
        pisteet = 0
        if tarkastettava.count(laatta) == 4:
            pisteet += 150 
        elif tarkastettava.count(laatta) == 3 and tarkastettava.count(0) == 1:
            pisteet += 20
        elif tarkastettava.count(laatta) == 2 and tarkastettava.count(0) == 2:
            pisteet += 10

        if tarkastettava.count(pelaajan_laatta) == 3 and tarkastettava.count(0) == 1:
            pisteet -= 100
            
        return pisteet
        

    #Annetaan enemmän pisteitä mitä edullisempi tilanne on tekoälyn kannalta
    def pisteyta(self, poyta, laatta):
        pisteet = 0
        keski_sarake = [poyta[i][3] for i in range(4)]
        keskella = keski_sarake.count(laatta)
        pisteet += keskella * 5
        
        #pisteytys vaakasuunnassa otetaan 4 mittaisia rivejä ja katsotaan sitten montako laattaa pelaajalla 2 eli AI:lla on

        for r in range(6):
            rivi_lista = [i for i in (poyta[r])]
            for s in range(4):
                tarkastettava = rivi_lista[s:s+4]
                pisteet += self.pisteet_rivista(tarkastettava, laatta)

        #pisteytys pystysuunnassa samalla tavalla kuin vaakasuunnassa
        for s in range(7):
            sarake_lista = []
            for r in range(6):
                sarake_lista.append(poyta[r][s])
            for r in range(3):
                tarkastettava = sarake_lista[r:r+4]
                pisteet += self.pisteet_rivista(tarkastettava, laatta)

        #pisteytys diagonaalissa samalla tavalla kuin 2 aikaisempaa
        for r in range(3):
            for s in range(4):
                tarkastettava = [poyta[r+i][s+i] for i in range(4)]
                pisteet += self.pisteet_rivista(tarkastettava, laatta)

        for r in range(3):
            for s in range(4):
                tarkastettava = [poyta[r+3-i][s+i] for i in range(4)]
                pisteet += self.pisteet_rivista(tarkastettava, laatta)

        return pisteet

    def loppu(self, poyta):
        return self.voiton_tarkistaja.onko_voittoa(poyta)[0] or len(self.mahdolliset_sarakkeet(self.pelipoyta)) == 0


    #minimax algoritmin toteutus pelaaja on pelaaja 1 ja tekoäly pelaaja 2
    def minimax(self, poyta, syvyys, a, b, maxPelaaja):
        mahdolliset = self.mahdolliset_sarakkeet(poyta)
        on_loppu = self.loppu(poyta)
        if syvyys == 0 or on_loppu:
            if on_loppu:
                if self.voiton_tarkistaja.onko_voittoa(poyta)[1] == 2:
                    print("2 pelaajalla voitto")
                    return None, 100000000
                elif self.voiton_tarkistaja.onko_voittoa(poyta)[1] == 1:
                    print("1 pelaajalla voitto")
                    return None, -100000000
                else:
                    return None, 0
            else:
                return None, self.pisteyta(poyta, 2)
        #maksivoivan pelaajan vuoro
        if maxPelaaja:
            pisteet = -math.inf
            sarake = random.choice(mahdolliset)
            for s in mahdolliset:
                rivi = self.seuraava_avoin_paikka(poyta, s)
                uusi_poyta = []
                #kopioi uuden pöydän
                for i in range(6):
                    uusi_poyta.append(poyta[i].copy())
                self.aseta_pala_taulukkoon(uusi_poyta, 2, rivi, s)
                uudet_pisteet = self.minimax(uusi_poyta, syvyys-1, a, b, False)[1]
                if uudet_pisteet > pisteet:
                    pisteet = uudet_pisteet
                    sarake = s
                #alpha beeta karsinta
                a = max(a, pisteet)
                if a >= b:
                    break                
            return sarake, pisteet
        #Minimoivan pelaajan vuoro
        else:
            pisteet = math.inf
            sarake = random.choice(mahdolliset)
            for s in mahdolliset:
                rivi = self.seuraava_avoin_paikka(poyta, s)
                uusi_poyta = []
                #kopioi uuden pöydän 
                for i in range(6):
                    uusi_poyta.append(poyta[i].copy())
                self.aseta_pala_taulukkoon(uusi_poyta, 1, rivi, s)
                uudet_pisteet = self.minimax(uusi_poyta, syvyys-1, a, b, True)[1]
                if uudet_pisteet < pisteet:
                    pisteet = uudet_pisteet
                    sarake = s
                #alpha beeta karsinta
                b = min(b, pisteet)
                if a >= b:
                    break
            return sarake, pisteet

    #asettaa palan kyseiseen kohtaan käytetään minimaxin toteutuksessa
    def aseta_pala_taulukkoon(self, taulukko, laatta, rivi, sarake):
        taulukko[rivi][sarake] = laatta

    #palauttaa kaikkien sarakkeiden numerot jonne voidaan vielä lisätä laatta eli ne jotka eivät ole täynnä
    def mahdolliset_sarakkeet(self, taulukko):
        mahdolliset = []
        for sarake in range(7):
            if self.voi_asettaa(sarake, taulukko):
                mahdolliset.append(sarake)
        return mahdolliset
            
    #AI:n peliliikkeen toteuttaminen
    def AI_peliliike(self):
        paras_kohta, pisteet = self.minimax(self.pelipoyta, 5, -math.inf, math.inf, True)
        print("parempi kohta ", paras_kohta)
        if self.voi_asettaa(paras_kohta, self.pelipoyta):
            self.pelisiirto(paras_kohta)
            self.AI_vuoro = False

    #etsii seuraavan tyhjän paikan pöydältä poyta
    def seuraava_avoin_paikka(self, poyta, sarake):
        for r in range(5,-1,-1):
            if poyta[r][sarake] == 0:
                return r

    #Pelin elossa pitävä silmukka
    def silmukka(self):
        while True:
            if self.AI_vuoro and self.AI_peli and not self.voitto:
                self.AI_peliliike()
                self.tutki_tapahtuma()
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
        impact = pygame.font.SysFont('impact', 50)
        impact_35 = pygame.font.SysFont('impact', 35)
        palaa = impact_35.render('Päävalikkoon', True, (YELLOW))
        if self.voitto:
            vuoro = impact.render(f'Pelaaja {self.voittaja} voitti!', True, YELLOW)
        elif self.tilanne == PELI:
            vuoro = impact.render(f'Pelaajan {self.pelaajan_vuoro.get_vuoro()} vuoro!', True, YELLOW)

        if self.tilanne == PELI:
            self.naytto.fill((20, 60, 200))
            for y in range(6):
                for x in range(7):
                    ruutu = self.pelipoyta[y][x]
                    self.naytto.blit(self.kuvat[ruutu], (x * 100, y*100+100))
                    self.naytto.blit(vuoro, (10,20))
                    self.naytto.blit(palaa, (450,30))

                    
            pygame.display.flip()
        
        elif self.tilanne == MENU:
            self.naytto.fill((255,255,255))
            s = pygame.font.SysFont('Impact',30)
            pelaa = s.render('Pelaa', True, (0,0,0))
            poistu = s.render('Poistu', True, (0,0,0))
            ai_peli = s.render('Pelaa tekoälyä vastaan', True, (0,0,0))
            #pygame.draw.rect(self.naytto, (0,200,30), (self.naytto.get_width()/7,self.naytto.get_height()/7,150,50))
            
            #pygame.draw.rect(self.naytto,(0,200,30), (self.naytto.get_width()/7,self.naytto.get_height()/2 - 200,150,50))
            
            self.naytto.blit(pelaa, (105,115))
            self.naytto.blit(poistu, (105,515))
            self.naytto.blit(ai_peli, (105,315))
            pygame.display.flip()


peli()