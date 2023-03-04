#vuoroa käsittelevä luokka
class Vuoro:
    def __init__(self) -> None:
        self.vuoro = 1

    def get_vuoro(self):
        return self.vuoro
    
    def get_vuoro_nimi(self):
        if self.vuoro == 1:
            return "Ismo"
        elif self.vuoro == 2:
            return "Seppo"
    
    def set_vuoro(self, vuoro):
        self.vuoro = vuoro
    
    #Vaihtaa pelaajan vuoroa
    def vaihda_vuoro(self):
        if self.vuoro == 1:
            self.vuoro = 2
        elif self.vuoro == 2:
            self.vuoro = 1
