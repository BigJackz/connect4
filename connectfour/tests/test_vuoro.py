import unittest
from vuoro import Vuoro

class TestVuoro(unittest.TestCase):
    def setUp(self) -> None:
        self.vuoro = Vuoro()
    
    def test_vaihda_vuoro_toimii_oikein(self):
        self.vuoro.vaihda_vuoro()
        self.assertEqual(self.vuoro.vuoro, 2)

    def test_vaihda_vuoro_toimii_oikein_vaihtaen_vuorosta_2_vuoroon_1(self):
        self.vuoro.vuoro = 2
        self.vuoro.vaihda_vuoro()
        self.assertEqual(self.vuoro.vuoro, 1)

    def test_get_vuoro_toimii_oikein(self):
        self.assertEqual(self.vuoro.get_vuoro(), 1)

    def test_set_vuoro_toimii_oikein(self):
        self.vuoro.set_vuoro(10)
        self.assertEqual(self.vuoro.get_vuoro(), 10)

    def test_get_vuoro_nimi_toimii_oikein_jos_vuoro_1(self):
        self.vuoro.vuoro = 1
        self.assertEqual(self.vuoro.get_vuoro_nimi(), "Ismo")

    def test_get_vuoro_nimi_toimii_oikein_jos_vuoro_2(self):
        self.vuoro.vuoro = 2
        self.assertEqual(self.vuoro.get_vuoro_nimi(), "Seppo")