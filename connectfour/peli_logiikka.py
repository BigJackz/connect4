from logiikka import VoitonTarkastaja
from logiikka import Vuoro
from minimax import Minimax
import math

MENU = 2
PELI = 1
VOITTO = 3
AI_VAIKEUSASTEEN_VALINTA = 4
NOVIISI = 1
ENNENKI = 3
MESTARI = 6

class Peli:
    def __init__(self) -> None:
        self.vuoro = Vuoro()
        self.tarkastaja = VoitonTarkastaja()
        self.minimax = Minimax()
        self.vaikeusaste = 1
        self.AI_vuoro = False
        self.AI_peli = False
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

    #Vaihtaa nykyisen pöydän tyhjään pöytään
    def tyhjenna_poyta(self):
        self.pelipoyta = [
            [0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
        ]

    #Debuggaus komento poistuu ennen viimeistä versiota
    #def piirra_poyta(self):
    #    for i in range(len(self.pelipoyta)):
    #        print(self.pelipoyta[i])

    def set_poyta(self, uusi):
        self.pelipoyta = uusi

    def get_poyta(self):
        return self.pelipoyta

    #tarkistaa onko ylimmällä rivillä kyseisellä sarakkellaa 0 jos on niin sinne voi vielä asettaa laatan
    def voi_asettaa(self, sarake, taulukko):
        if taulukko[0][sarake] == 0:
            return True
        else:
            return False

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
        
    #Asettaa laatan sarakkeeseen jos voi ja vaihtaa vuoron
    def aseta_pala(self, sarake):
        for i in range(5,-1,-1):
            if self.pelipoyta[i][sarake] == 0:
                self.pelipoyta[i][sarake] = self.vuoro.get_vuoro() #asetetaan self.pelaajaa vastaava laatta paikoilleen
                break

        #Tarkistaa lopuksi onko jonpi kumpi pelaajista voittanut pelin
        self.voittaja, self.voitto = self.tarkastaja.voiton_tarkastaja(self.pelipoyta)

    #Pelisiirto tarkistaa koordinaateista mihinkä kohtaan pelaaja on asettamassa laattaa ja asettaa sen siihen kohtaan x koordinaatteja 
    def pelisiirto(self, sarake):
        if self.voi_asettaa(sarake, self.pelipoyta):
            self.aseta_pala(sarake)
            self.vuoro.vaihda_vuoro()
            if self.AI_peli:
                self.AI_vuoro = True


    #Ottaa pygamen koordinaatit tuplen ja palauttaa int arvon joka vastaa saraketta alkaen arvosta 0 arvoon 6
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

    #AI:n peliliikkeen toteuttaminen
    def AI_peliliike(self):
        paras_kohta, pisteet = self.minimax.minimax(self.pelipoyta, self.vaikeusaste, -math.inf, math.inf, True)
        if paras_kohta == None:
            #TODO
            #jos paras_kohta == 0, niin minimax ei löydä kohtaa johon laittaa palaa joten pelipoytä on täysi ja peli päättyy tasapeliin
            #se on lisättävä tähän kohtaan
            #vaihdetaan paras_kohta nonesta takaisin int arvoksi että voi_asettaa ei yritä etsiä listasta indeksillä none
            paras_kohta = 0
        elif self.voi_asettaa(paras_kohta, self.pelipoyta):
           self.pelisiirto(paras_kohta)
           self.AI_vuoro = False

    #palauttaa arvot joita käytetään ainakin vielä pelin käyttöliittymän koodissa
    def palauta_arvot(self):
        return self.vuoro.get_vuoro(), self.tilanne
    
    def alusta_arvot(self):
        self.voitto = False
        self.AI_peli = False
        self.vuoro.set_vuoro(1)
        self.tyhjenna_poyta()

    #Vaihtaa arvot sellaisiksi että peli alkaa AI:ta vastaan
    def pelin_alustaminen_ai_vastaan(self):
        self.tilanne = PELI
        self.alusta_arvot()
        self.AI_peli = True

    #Vaihtaa arvot sellaisiksi että peli alkaa 1v1 toista pelaajaa vastaan
    def aloita_1v1_peli(self):
        self.tilanne = PELI
        self.alusta_arvot()

    #Vaihtaa arvot sellaisiksi että peli menee takaisin päävalikkoon
    def paavalikkoon(self):
        self.tilanne = MENU
        self.alusta_arvot()

    #Vaihtaa pelin tilan ai peliksi
    def ai_peli(self):
        self.tilanne = AI_VAIKEUSASTEEN_VALINTA

    #Vaihtaa vaikeusastetta arvoon vaikeus
    def vaihda_ai_vaikeustaso(self, vaikeus):
        self.vaikeusaste = vaikeus

    def onko_ai_vuoro(self):
        return self.AI_vuoro
    
    def onko_ai_peli(self):
        return self.AI_peli
    
    def palauta_tilanne(self):
        return self.tilanne
    
    def aseta_tilanne(self, tilanne):
        self.tilanne = tilanne
    
    def palauta_voittaja(self):
        return self.voittaja
    
    def palauta_onko_voittoa(self):
        return self.voitto