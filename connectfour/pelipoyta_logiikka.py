#Pelipoytaa käsittelevä luokka
class PeliPoytaLogiikka():
    def __init__(self) -> None:
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

    def set_poyta(self, uusi):
        self.pelipoyta = uusi

    def get_poyta(self):
        return self.pelipoyta
    
    #Tarkistaa onko ylimmällä rivillä kyseisellä sarakkellaa 0 jos on niin sinne voi vielä asettaa laatan
    def voi_asettaa(self, sarake, taulukko):
        if taulukko[0][sarake] == 0:
            return True
        else:
            return False
        
    #Asettaa laatan sarakkeeseen, jos voi ja vaihtaa vuoron
    def aseta_pala(self, sarake, pelaaja):
        for i in range(5,-1,-1):
            if self.pelipoyta[i][sarake] == 0:
                self.pelipoyta[i][sarake] = pelaaja #Asetetaan self.pelaajaa vastaavan laatan paikoilleen
                break

    #Etsii seuraavan tyhjän paikan pöydältä poyta
    def seuraava_avoin_paikka(self, poyta, sarake):
        for r in range(5,-1,-1):
            if poyta[r][sarake] == 0:
                return r
            
    #Asettaa palan kyseiseen kohtaan käytetään minimaxin toteutuksessa
    def aseta_pala_taulukkoon(self, taulukko, laatta, rivi, sarake):
        taulukko[rivi][sarake] = laatta

    #Palauttaa kaikkien sarakkeiden numerot jonne voidaan vielä lisätä laatta eli ne, jotka eivät ole täynnä
    def mahdolliset_sarakkeet(self, taulukko):
        mahdolliset = []
        for sarake in range(7):
            if self.voi_asettaa(sarake, taulukko):
                mahdolliset.append(sarake)
        return mahdolliset

    def print_poyta(self):
        for i in range(6):
            print(self.pelipoyta[i])