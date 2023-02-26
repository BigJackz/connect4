import random
import math
from logiikka import VoitonTarkastaja

class Minimax:
    def __init__(self) -> None:
        self.voiton_tarkastaja = VoitonTarkastaja()

    #Terminaali tapauksen tarkistaminen eli tarkistaa saavuttaako kumpikaan pelaaja voittoa tai onko mahdollisia sarakkeita jäljellä 0 jos on niin pelipöytä on täynnä ja peli päättyy tasapeliin
    def loppu(self, poyta):
        return self.voiton_tarkastaja.onko_voittoa(poyta)[0] or len(self.mahdolliset_sarakkeet(poyta)) == 0

    #palauttaa kaikkien sarakkeiden numerot jonne voidaan vielä lisätä laatta eli ne jotka eivät ole täynnä
    def mahdolliset_sarakkeet(self, taulukko):
        mahdolliset = []
        for sarake in range(7):
            if self.voi_asettaa(sarake, taulukko):
                mahdolliset.append(sarake)
        return mahdolliset

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
            pisteet += 100
        elif tarkastettava.count(laatta) == 3 and tarkastettava.count(0) == 1:
            pisteet += 10
        elif tarkastettava.count(laatta) == 2 and tarkastettava.count(0) == 2:
            pisteet += 5

        if tarkastettava.count(pelaajan_laatta) == 3 and tarkastettava.count(0) == 1:
            pisteet -= 70
            
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

    #etsii seuraavan tyhjän paikan pöydältä poyta
    def seuraava_avoin_paikka(self, poyta, sarake):
        for r in range(5,-1,-1):
            if poyta[r][sarake] == 0:
                return r

    #asettaa palan kyseiseen kohtaan käytetään minimaxin toteutuksessa
    def aseta_pala_taulukkoon(self, taulukko, laatta, rivi, sarake):
        taulukko[rivi][sarake] = laatta

    #minimax algoritmin toteutus pelaaja on pelaaja 1 ja tekoäly pelaaja 2
    def minimax(self, poyta, syvyys, a, b, maxPelaaja):
        mahdolliset = self.mahdolliset_sarakkeet(poyta)
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
