from logiikka import voiton_tarkastaja
import unittest
from logiikka import vuoro

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
        self.v = voiton_tarkastaja()

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

class TestVuoro(unittest.TestCase):
    def setUp(self) -> None:
        self.vuoro = vuoro()
        return super().setUp()
    
    def test_vuoron_vaihtaminen_toimii_oikein(self):
        self.vuoro.vaihda_vuoro()
        self.vuoro.vaihda_vuoro()
        self.assertEqual(self.vuoro.get_vuoro(), 1)

    def test_vuoron_get_vuoro_toimii_oikein(self):
        self.assertEqual(self.vuoro.get_vuoro(), 1)

    def test_vuoron_asettaminen_set_vuoro_toimii_oikein(self):
        self.vuoro.set_vuoro(10)
        self.assertEqual(self.vuoro.get_vuoro(), 10)