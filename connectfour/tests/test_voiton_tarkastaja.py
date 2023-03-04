from voiton_tarkastaja import VoitonTarkastaja
import unittest


class TestVoitto(unittest.TestCase):
    def setUp(self) -> None:
        self.poyta = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
            
        ]
        self.poyta1 = [
            [2,1,2,1,2,1,2],
            [0,0,0,0,0,0,0],
            [1,2,1,2,1,2,1],
            [0,0,0,0,0,0,0],
            [1,2,1,2,1,2,1],
            [2,1,2,1,2,1,2]
        ]
        self.poyta2 = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,2,0,0,0],
            [0,0,0,2,0,0,0],
            [1,0,0,2,0,0,0],
            [1,1,1,2,2,2,2]
        ]
        self.poyta3 = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1],
            [0,1,1,1,1,0,1],
            [0,2,1,2,2,0,1],
            [0,1,2,1,2,0,1]
        ]
        self.poyta4 = [
            [1,2,2,1,2,1,1],
            [1,2,1,2,1,2,1],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,2,2,2,2,0,0]
        ]
        self.poyta5 = [
            [0,1,0,0,1,0,0],
            [1,0,1,0,1,0,0],
            [0,0,0,0,0,0,0],
            [1,0,1,0,1,0,0],
            [1,0,0,0,0,0,0],
            [0,1,1,0,1,0,1]
        ]
        self.poyta6 = [
            [0,0,0,2,0,0,0],
            [1,0,0,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,0,1,0,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0]
        ]
        self.poyta7 = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,2],
            [0,1,0,0,0,2,1],
            [1,1,0,0,2,1,1],
            [0,0,0,2,1,2,1]
        ]
        self.poyta8 = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,1,1,2,2,2,2]
        ]
        self.poyta9 = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
            [2,0,0,1,0,0,0],
            [2,2,2,1,0,2,2]
        ]
        self.diagonaalipoyta1 =[
            [1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,2,0,0,0,0],
            [0,0,0,2,0,0,0],
            [0,0,0,0,2,0,0],
            [0,0,0,0,0,2,0],
        ]
        self.diagonaalipoyta2 = [
            [1,0,0,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,0,1,0,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,0,2,0,0],
            [0,0,0,0,0,2,0],
        ]
        self.diagonaalipoyta3 = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [2,1,0,0,0,0,0],
            [0,2,0,0,0,0,0],
            [0,0,2,0,0,0,0],
            [0,0,0,2,0,0,0],
        ]
        self.diagonaalipoyta4 = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,0,1,0,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,0,1],
        ]
        self.diagonaalipoyta5 = [
            [0,0,0,2,0,0,0],
            [0,0,0,0,2,0,0],
            [0,0,0,2,0,2,0],
            [0,0,0,0,1,0,2],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,0,1],
        ]
        self.diagonaalipoyta6 = [
            [0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0],
            [0,0,0,0,2,0,0],
            [0,0,0,2,0,0,0],
            [0,0,2,0,0,0,0],
            [0,2,0,0,0,0,0],
        ]
        self.diagonaalipoyta7 = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0],
            [0,2,0,0,0,0,0],
        ]
        self.diagonaalipoyta8 = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0],
        ]
        self.diagonaalipoyta9 = [
            [0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0],
            [0,1,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
        ]
        self.diagonaalipoyta10 = [
            [0,0,0,0,0,2,0],
            [0,0,1,0,2,0,0],
            [0,1,0,2,0,0,0],
            [1,0,2,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
        ]

        self.v = VoitonTarkastaja()


    def test_voitto_vaakasuunnassa_voitto_alimalla_rivilla_pelaajalla_2(self):
        self.assertEqual(self.v.voitto_vaakasuunnassa(self.poyta2), (True,2))
    
    def test_ei_voittoa_vaakasuunnassa_missään(self):
        self.assertEqual(self.v.voitto_vaakasuunnassa(self.poyta1), (False,0))

    def test_voitto_vaakasuunnassa_3_rivilla_pelaajalla_1(self):
        self.assertEqual(self.v.voitto_vaakasuunnassa(self.poyta3), (True,1))

    def test_ei_voittoa_vaakasuunnassa_koska_tyhja_pelipoyta(self):
        self.assertEqual(self.v.voitto_vaakasuunnassa(self.poyta), (False,0))

    def test_voitto_vaakasuunnassa_rivillä_1_pelaajalla_2(self):
        self.assertEqual(self.v.voitto_vaakasuunnassa(self.poyta4), (True,2))
    
    def test_ei_voittoa_hamarassa_poydassa_vaakasuunnassa(self):
        self.assertEqual(self.v.voitto_vaakasuunnassa(self.poyta5), (False,0))

    def test_ei_voittoa_pystysuunnassa_koska_tyhja_poyta(self):
        self.assertEqual(self.v.voitto_pystysuunnassa(self.poyta), (False,0))

    def test_voitto_pystysuunnassa_sarakkeessa_4_pelaajalla_2(self):
        self.assertEqual(self.v.voitto_pystysuunnassa(self.poyta2), (True,2))

    def test_voitto_pystysuunnassa_sarakkeessa_7_pelaajalla_1(self):
        self.assertEqual(self.v.voitto_pystysuunnassa(self.poyta3), (True,1))

    def test_ei_voittoa_hamarassa_poydassa_pystysuunnassa(self):
        self.assertEqual(self.v.voitto_pystysuunnassa(self.poyta5), (False,0))

    def test_ei_voittoa_hamarassa_poydassa_diagonaalissa(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.poyta5), (False,0))

    def test_ei_voittoa_diagonaalissa_tyhjalla_poydalla(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.poyta), (False,0))
    
    def test_voitto_diagonaalissa_pelaajalla_1(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.poyta6), (True,1))

    def test_voitto_diagonaalissa_pelaajalla_2(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.poyta7), (True,2))

    def test_onko_voittoa_toimii_oikein_voitolla_diagonaalissa(self):
        self.assertEqual(self.v.onko_voittoa(self.poyta7), (True, 2))

    def test_onko_voittoa_toimii_oikein_voitolla_vaakasuunnassa(self):
        self.assertEqual(self.v.onko_voittoa(self.poyta8), (True, 2))

    def test_voiton_tarkastaja_toimii_oikein_voitolla_vaakasuunnassa(self):
        self.assertEqual(self.v.voiton_tarkastaja(self.poyta8), (2, True))

    def test_voiton_tarkastaja_toimii_oikein_voitolla_pystysuunnassa(self):
        self.assertEqual(self.v.voiton_tarkastaja(self.poyta9), (1, True))

    def test_voiton_tarkastaja_toimii_oikein_voitolla_diagonaalissa(self):
        self.assertEqual(self.v.voiton_tarkastaja(self.poyta7), (2, True))

    def test_voitto_diagonaalissa_loytaa_voiton_oikein(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.diagonaalipoyta1), (True, 2))

    def test_voitto_diagonaalissa_loytaa_voiton_oikein_tilanne2(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.diagonaalipoyta2), (True, 1))

    def test_voitto_diagonaalissa_loytaa_voiton_oikein_tilanne3(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.diagonaalipoyta3), (True, 2))

    def test_voitto_diagonaalissa_loytaa_voiton_oikein_tilanne4(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.diagonaalipoyta4), (True, 1))
    
    def test_voitto_diagonaalissa_loytaa_voiton_oikein_tilanne5(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.diagonaalipoyta5), (True, 2))

    def test_voitto_diagonaalissa_loytaa_voiton_oikein_tilanne6(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.diagonaalipoyta6), (True, 2))

    def test_voitto_diagonaalissa_loytaa_voiton_oikein_tilanne7(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.diagonaalipoyta7), (True, 1))

    def test_voitto_diagonaalissa_loytaa_voiton_oikein_tilanne8(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.diagonaalipoyta8), (True, 1))

    def test_voitto_diagonaalissa_loytaa_voiton_oikein_tilanne9(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.diagonaalipoyta9), (True, 1))

    def test_voitto_diagonaalissa_loytaa_voiton_oikein_tilanne10(self):
        self.assertEqual(self.v.voitto_diagonaalissa(self.diagonaalipoyta10), (True, 2))
