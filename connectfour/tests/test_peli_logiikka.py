import unittest
from peli_logiikka import Peli


class TestPeli(unittest.TestCase):
    def setUp(self) -> None:
        self.peli = Peli()
        self.poyta = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
        ]

    def test_sarake_koordinaateista_toimii_oikein_antaen_sarakkeen_1(self):
        self.assertEqual(self.peli.sarake_koordinaateista((120,410)), 1)

    def test_sarake_koordinaateista_toimii_oikein_antaen_sarakkeen_0(self):
        self.assertEqual(self.peli.sarake_koordinaateista((3,553)), 0)

    def test_AI_peliliike_voittaa_pelin_jos_seuraavalla_siirrolla_voitto(self):
        self.peli.poyta.set_poyta([
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [2,0,0,0,0,0,0],
            [2,0,0,0,0,0,0],
            [2,0,0,0,0,0,0]
        ])
        self.peli.vuoro.vuoro = 2
        self.peli.AI_peliliike()
        self.assertEqual(self.peli.poyta.pelipoyta, [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [2,0,0,0,0,0,0],
            [2,0,0,0,0,0,0],
            [2,0,0,0,0,0,0],
            [2,0,0,0,0,0,0]
        ])

    def test_AI_peliliike_ei_tee_mitaan_jos_ei_voi_asettaa(self):
        self.peli.poyta.pelipoyta = [[1, 10, 6, 10, 10, 10, 2], [9, 5, 7, 9, 4, 8, 1], [8, 4, 2, 5, 1, 2, 8], [9, 1, 3, 4, 4, 10, 2], [9, 1, 5, 5, 3, 6, 6], [3, 2, 6, 8, 5, 7, 5]]
        self.peli.AI_vuoro = True
        self.peli.AI_peliliike()
        self.assertEqual(self.peli.AI_vuoro, True)
    
    def test_palauta_tilanne_toimii_oikein(self):
        self.assertEqual(self.peli.palauta_tilanne(), 2)

    def test_ai_peli_toimii_oikein(self):
        self.peli.ai_peli()
        self.assertEqual(self.peli.palauta_tilanne(), 4)

    def test_palauta_onko_voittoa_toimii_oikein(self):
        self.assertEqual(self.peli.palauta_onko_voittoa(), False)

    def test_palauta_voittaja_toimii_oikein_kun_ei_voittoa_kummallakaan(self):
        self.assertEqual(self.peli.palauta_voittaja(), 0)

    def test_palauta_voittaja_toimii_oikein_kun_voittaja_on_selvilla(self):
        self.peli.voittaja = 1
        self.assertEqual(self.peli.palauta_voittaja(), 1)

    def test_aseta_tilanne_toimii_oikein(self):
        self.peli.aseta_tilanne(4)
        self.assertEqual(self.peli.tilanne, 4)

    def test_onko_ai_peli_toimii_oikein(self):
        self.peli.AI_peli = True
        self.assertEqual(self.peli.onko_ai_peli(), True)

    def test_onko_ai_vuoro_toimii_oikein(self):
        self.peli.AI_vuoro = True
        self.assertEqual(self.peli.onko_ai_vuoro(), True)

    def test_vaihda_ai_vaikeusaste_toimii_oikein(self):
        self.peli.vaihda_ai_vaikeustaso(10)
        self.assertEqual(self.peli.vaikeusaste, 10)

    def test_paavalikkoon_vaihtaa_arvot_oiken(self):
        self.peli.tilanne = 10
        self.peli.voitto = True
        self.peli.AI_peli = True
        self.peli.vuoro.set_vuoro(2)
        self.peli.poyta.pelipoyta = [
            [0,0,0,4,0,0,0],
            [0,2,0,0,0,0,0],
            [0,0,0,0,5,0,0],
            [0,0,1,0,0,0,0],
            [0,2,1,0,0,0,0],
            [0,1,1,0,0,0,0]
        ]
        self.peli.paavalikkoon()
        self.assertEqual(self.peli.tilanne, 2)
        self.assertEqual(self.peli.voitto, False)
        self.assertEqual(self.peli.AI_peli, False)
        self.assertEqual(self.peli.vuoro.vuoro, 1)
        self.assertEqual(self.peli.poyta.pelipoyta, [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
        ])

    def test_aloita_1v1_peli_vaihtaa_arvot_oikein(self):
        self.peli.voitto = True
        self.peli.AI_peli = True
        self.peli.poyta.pelipoyta = [
            [0,0,0,4,0,0,0],
            [0,2,0,0,0,0,0],
            [0,0,0,0,5,0,0],
            [0,0,1,0,0,0,0],
            [0,2,1,0,0,0,0],
            [0,1,1,0,0,0,0]
        ]
        self.peli.tilanne = 3
        self.peli.vuoro.set_vuoro(2)
        self.peli.aloita_1v1_peli()
        self.assertEqual(self.peli.voitto, False)
        self.assertEqual(self.peli.AI_peli, False)
        self.assertEqual(self.peli.poyta.pelipoyta, [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
        self.assertEqual(self.peli.tilanne, 1)
        self.assertEqual(self.peli.vuoro.vuoro, 1)

    def test_pelin_alustaminen_ai_vastaan_vaihtaa_arvot_oikein(self):
        self.peli.vuoro.set_vuoro(2)
        self.peli.voitto = True
        self.peli.poyta.pelipoyta = [[0,0,0,1,0,0,0],[0,2,0,0,0,0,0],[0,0,0,0,0,3,0],[0,0,0,0,0,0,4],[0,0,1,2,2,0,0],[0,0,0,1,1,1,1]]
        self.peli.tilanne = 5
        self.peli.AI_peli = False
        self.peli.pelin_alustaminen_ai_vastaan()
        self.assertEqual(self.peli.vuoro.vuoro, 1)
        self.assertEqual(self.peli.voitto, False)
        self.assertEqual(self.peli.poyta.pelipoyta, [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
        self.assertEqual(self.peli.tilanne, 1)
        self.assertEqual(self.peli.AI_peli, True)

    def test_pelisiirto_asettaa_palan_ja_vaihtaa_vuoron(self):
        self.peli.pelisiirto(2)
        self.assertEqual(self.peli.vuoro.vuoro, 2)
        self.assertEqual(self.peli.poyta.pelipoyta, [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,0]])
    
    def test_pelisiirto_vaihtaa_ai_vuoron_jos_ai_peli(self):
        self.peli.AI_peli = True
        self.peli.pelisiirto(2)
        self.assertEqual(self.peli.AI_vuoro, True)

    def test_pelisiirto_ei_tee_mitaan_jos_ei_voi_asettaa(self):
        self.peli.poyta.pelipoyta = [[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0]]
        self.peli.pelisiirto(0)
        self.assertEqual(self.peli.vuoro.vuoro, 1)