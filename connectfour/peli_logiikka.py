from voiton_tarkastaja import VoitonTarkastaja
from vuoro import Vuoro
from minimax import Minimax
import math
from pelipoyta_logiikka import PeliPoytaLogiikka

MENU = 2
PELI = 1
AI_VAIKEUSASTEEN_VALINTA = 4
NOVIISI = 1

class Peli:
    def __init__(self) -> None:
        self.vuoro = Vuoro()
        self.tarkastaja = VoitonTarkastaja()
        self.minimax = Minimax()
        self.poyta = PeliPoytaLogiikka()
        self.AI_vuoro = False
        self.AI_peli = False
        self.vaikeusaste = NOVIISI
        self.tilanne = MENU
        self.voittaja = 0
        self.voitto = False

    #Pelisiirto tarkistaa koordinaateista mihinkä kohtaan pelaaja on asettamassa laattaa ja asettaa sen siihen kohtaan x koordinaatteja 
    def pelisiirto(self, sarake):
        if self.poyta.voi_asettaa(sarake, self.poyta.get_poyta()):
            self.poyta.aseta_pala(sarake, self.vuoro.get_vuoro())
            self.voittaja, self.voitto = self.tarkastaja.voiton_tarkastaja(self.poyta.get_poyta()) #Tarkistaa onko jonpi kumpi pelaajista voittanut pelin
            self.vuoro.vaihda_vuoro()
            if self.AI_peli:
                self.AI_vuoro = True

    #Ottaa pygamen koordinaatit tuplen ja palauttaa int arvon joka vastaa saraketta alkaen arvosta 0 arvoon 6
    def sarake_koordinaateista(self, koordinaatit):
        x_koordinaatti = koordinaatit[0]
        x = str(x_koordinaatti)
        uusi_x = x[0]
        sarake = int(uusi_x)
        if len(x) < 3:
            return 0
        else:
            return sarake

    #AI:n peliliikkeen toteuttaminen
    def AI_peliliike(self):
        paras_kohta, pisteet = self.minimax.minimax(self.poyta.get_poyta(), self.vaikeusaste, -math.inf, math.inf, True)
        if paras_kohta == None:
            #jos paras_kohta == None, niin minimax ei löydä kohtaa johon laittaa palaa joten pelipoytä on täysi ja peli päättyy tasapeliin
            #vaihdetaan paras_kohta nonesta takaisin int arvoksi että voi_asettaa ei yritä etsiä listasta indeksillä none
            paras_kohta = 0
        elif self.poyta.voi_asettaa(paras_kohta, self.poyta.get_poyta()):
           self.pelisiirto(paras_kohta)
           self.AI_vuoro = False

    #Vaihtaa pelin muuttujien arvot niin, että voidaan aloittaa peli
    def alusta_arvot(self):
        self.voitto = False
        self.AI_peli = False
        self.vuoro.set_vuoro(1)
        self.poyta.tyhjenna_poyta()

    #Vaihtaa muuttujien arvot sellaisiksi, että peli alkaa AI:ta vastaan
    def pelin_alustaminen_ai_vastaan(self):
        self.tilanne = PELI
        self.alusta_arvot()
        self.AI_peli = True

    #Vaihtaa muuttujien arvot sellaisiksi, että peli alkaa 1v1 toista pelaajaa vastaan
    def aloita_1v1_peli(self):
        self.tilanne = PELI
        self.alusta_arvot()

    #Vaihtaa arvot sellaisiksi, että peli menee takaisin päävalikkoon
    def paavalikkoon(self):
        self.tilanne = MENU
        self.alusta_arvot()

    #Vaihtaa pelin tilan AI peliksi
    def ai_peli(self):
        self.tilanne = AI_VAIKEUSASTEEN_VALINTA

    #Vaihtaa vaikeusastetta parametriin vaikeus
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
    
    #Tarkistaa onko ylimmän rivin nollien määrä nolla, jos on pelilauta on täysi ja palauta True, muutoin False
    def onko_tasapeli(self):
        rivi = self.poyta.get_poyta()[0]
        if rivi.count(0) == 0:
            return True
        else:
            return False