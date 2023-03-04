import unittest
from pelipoyta_logiikka import PeliPoytaLogiikka

class TestPeliPoytaLogiikka(unittest.TestCase):
    def setUp(self) -> None:
        self.poyta_logiikka = PeliPoytaLogiikka()

    def test_get_poyta_toimii_oikein(self):
        self.assertEqual(self.poyta_logiikka.get_poyta(), [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
        ])

    def test_set_poyta_toimii_oikein(self):
        uusi = [
            [0,0,0,0,0,0,0],
            [0,1,2,0,0,0,0],
            [0,1,1,0,0,0,0],
            [0,2,2,0,0,0,0],
            [0,1,2,0,0,0,0],
            [0,1,2,0,0,0,0]
        ]
        self.poyta_logiikka.set_poyta(uusi)
        self.assertEqual(self.poyta_logiikka.pelipoyta, [
            [0,0,0,0,0,0,0],
            [0,1,2,0,0,0,0],
            [0,1,1,0,0,0,0],
            [0,2,2,0,0,0,0],
            [0,1,2,0,0,0,0],
            [0,1,2,0,0,0,0]
        ])

    def test_tyhjenna_poyta_toimii_oikein(self):
        self.poyta_logiikka.set_poyta([
            [0,0,0,0,0,0,0],
            [0,1,2,0,0,0,0],
            [0,1,1,0,0,0,0],
            [0,2,2,0,0,0,0],
            [0,1,2,0,0,0,0],
            [0,1,2,0,0,0,0]
        ])
        self.poyta_logiikka.tyhjenna_poyta()
        self.assertEqual(self.poyta_logiikka.pelipoyta, [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
        ])

    def test_voi_asettaa_toimii_oikein_palauttaen_false(self):
        self.poyta_logiikka.pelipoyta = [
            [0,0,1,0,0,0,0],
            [0,0,1,0,0,0,0],
            [0,0,1,0,0,0,0],
            [0,0,1,0,0,0,0],
            [0,0,1,0,0,0,0],
            [0,0,1,0,0,0,0]
        ]
        self.assertEqual(self.poyta_logiikka.voi_asettaa(2, self.poyta_logiikka.pelipoyta), False)

    def test_voi_asettaa_toimii_oikein_palauttaen_true(self):
        self.assertEqual(self.poyta_logiikka.voi_asettaa(3, self.poyta_logiikka.pelipoyta), True)