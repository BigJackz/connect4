import random
import math
from voiton_tarkastaja import VoitonTarkastaja
from ai_pisteytys import Pisteet
from pelipoyta_logiikka import PeliPoytaLogiikka

class Minimax:
    def __init__(self) -> None:
        self.voiton_tarkastaja = VoitonTarkastaja()
        self.pisteet = Pisteet()
        self.poyta = PeliPoytaLogiikka()

    #Terminaali tapauksen tarkistaminen eli tarkistaa saavuttaako kumpikaan pelaaja voittoa tai onko mahdollisia sarakkeita jäljellä 0 jos on niin pelipöytä on täynnä ja peli päättyy tasapeliin
    def loppu(self, poyta):
        return self.voiton_tarkastaja.onko_voittoa(poyta)[0] or len(self.poyta.mahdolliset_sarakkeet(poyta)) == 0

    #minimax algoritmin toteutus pelaaja on pelaaja 1 ja tekoäly pelaaja 2
    def minimax(self, poyta, syvyys, a, b, maxPelaaja):
        mahdolliset = self.poyta.mahdolliset_sarakkeet(poyta)
        on_loppu = self.loppu(poyta)
        if syvyys == 0 or on_loppu:
            if on_loppu:
                if self.voiton_tarkastaja.onko_voittoa(poyta)[1] == 2:
                    return None, 1000000000
                elif self.voiton_tarkastaja.onko_voittoa(poyta)[1] == 1:
                    return None, -1000000000
                else:
                    return None, 0
            else:
                return None, self.pisteet.pisteyta(poyta, 2)
        #maksivoivan pelaajan vuoro
        if maxPelaaja:
            pisteet = -math.inf
            sarake = random.choice(mahdolliset)
            for s in mahdolliset:
                rivi = self.poyta.seuraava_avoin_paikka(poyta, s)
                uusi_poyta = []
                #kopioi uuden pöydän
                for i in range(6):
                    uusi_poyta.append(poyta[i].copy())
                self.poyta.aseta_pala_taulukkoon(uusi_poyta, 2, rivi, s)
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
                rivi = self.poyta.seuraava_avoin_paikka(poyta, s)
                uusi_poyta = []
                #kopioi uuden pöydän
                for i in range(6):
                    uusi_poyta.append(poyta[i].copy())
                self.poyta.aseta_pala_taulukkoon(uusi_poyta, 1, rivi, s)
                uudet_pisteet = self.minimax(uusi_poyta, syvyys-1, a, b, True)[1]
                if uudet_pisteet < pisteet:
                    pisteet = uudet_pisteet
                    sarake = s
                #alpha beeta karsinta
                b = min(b, pisteet)
                if a >= b:
                    break
            return sarake, pisteet
