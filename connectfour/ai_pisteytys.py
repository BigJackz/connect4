
class Pisteet:
    def __init__(self) -> None:
        pass

    #Annetaan enemmän pisteitä mitä edullisempi tilanne on tekoälyn kannalta
    def pisteyta(self, poyta, laatta):
        pisteet = 0
        keski_sarake = [poyta[i][3] for i in range(4)]
        keskella = keski_sarake.count(laatta)
        pisteet += keskella * 3

        #Pisteytys vaakasuunnassa otetaan 4 mittaisia rivejä ja katsotaan sitten montako laattaa pelaajalla 2 eli AI:lla on
        for r in range(6):
            rivi_lista = [i for i in (poyta[r])]
            for s in range(4):
                tarkastettava = rivi_lista[s:s+4]
                pisteet += self.pisteet_rivista(tarkastettava, laatta)

        #Pisteytys pystysuunnassa samalla tavalla kuin vaakasuunnassa
        for s in range(7):
            sarake_lista = []
            for r in range(6):
                sarake_lista.append(poyta[r][s])
            for r in range(3):
                tarkastettava = sarake_lista[r:r+4]
                pisteet += self.pisteet_rivista(tarkastettava, laatta)

        #Pisteytys diagonaalissa samalla tavalla kuin 2 aikaisempaa
        for r in range(3):
            for s in range(4):
                tarkastettava = [poyta[r+i][s+i] for i in range(4)]
                pisteet += self.pisteet_rivista(tarkastettava, laatta)

        for r in range(3):
            for s in range(4):
                tarkastettava = [poyta[r+3-i][s+i] for i in range(4)]
                pisteet += self.pisteet_rivista(tarkastettava, laatta)

        return pisteet
    
    #Annetaan pisteitä siitä kuinka hyvä pelitilanne on pelaajalle 2 eli AI:lle
    def pisteet_rivista(self, tarkastettava, laatta):
        pelaajan_laatta = 1
        pisteet = 0

        if tarkastettava.count(laatta) == 4:
            pisteet += 100
            
        elif tarkastettava.count(laatta) == 3 and tarkastettava.count(pelaajan_laatta) == 1:
            pisteet += 50

        elif tarkastettava.count(laatta) == 3 and tarkastettava.count(0) == 1:
            pisteet += 30

        elif tarkastettava.count(laatta) == 2 and tarkastettava.count(pelaajan_laatta) == 1:
            pisteet += 25

        elif tarkastettava.count(laatta) == 2 and tarkastettava.count(0) == 2:
            pisteet += 10

        if tarkastettava.count(pelaajan_laatta) == 3 and tarkastettava.count(0) == 1:
            pisteet -= 80
            
        return pisteet