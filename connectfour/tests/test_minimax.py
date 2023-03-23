import unittest
from minimax import Minimax
from peli_logiikka import Peli

class TestPeli(unittest.TestCase):
    def setUp(self) -> None:
        self.peli = Peli()
        self.peli.vaikeusaste = 6
        self.peli.vuoro.set_vuoro(2)

    def test_minimax_voittaa_tilanteessa_1(self):
        self.peli.poyta.set_poyta([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,2,2,0,1]])
        self.peli.AI_peliliike()
        self.peli.pelisiirto(1)
        self.peli.AI_peliliike()
        self.assertEqual(self.peli.poyta.get_poyta(), [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,0,0,0,1],[0,1,2,2,2,2,1]])

    def test_minimax_voittaa_yksin_neljalla_siirrolla(self):
        self.peli.AI_peliliike()
        self.peli.vuoro.set_vuoro(2)
        self.peli.AI_peliliike()
        self.peli.vuoro.set_vuoro(2)
        self.peli.AI_peliliike()
        self.peli.vuoro.set_vuoro(2)
        self.peli.AI_peliliike()
        self.assertEqual(self.peli.poyta.get_poyta(), [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[2,2,2,2,0,0,0]])

    def test_minimax_voittaa_tilanteessa_2(self):
        self.peli.poyta.set_poyta([[0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 1],
                                   [0, 0, 0, 0, 2, 1, 1],
                                   [0, 0, 1, 2, 1, 1, 1]])
        self.peli.AI_peliliike()
        self.peli.vuoro.vaihda_vuoro()
        self.peli.AI_peliliike()
        self.assertEqual(self.peli.poyta.get_poyta(), [[0, 0, 0, 0, 0, 0, 0],
                                                       [0, 0, 0, 0, 0, 0, 0],
                                                       [0, 0, 0, 0, 0, 0, 2],
                                                       [0, 0, 0, 0, 0, 2, 1],
                                                       [0, 0, 0, 0, 2, 1, 1],
                                                       [0, 0, 1, 2, 1, 1, 1]])
        
    def test_minimax_voittaa_tilanteessa_3(self):
        self.peli.poyta.set_poyta([ [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 2, 0, 0, 0],
                                    [0, 1, 1, 2, 1, 0, 0]])
        self.peli.AI_peliliike()
        self.peli.vuoro.vaihda_vuoro()
        self.peli.AI_peliliike()
        self.assertEqual(self.peli.poyta.get_poyta(), [ [0, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 0, 2, 0, 0, 0],
                                                        [0, 0, 0, 2, 0, 0, 0],
                                                        [0, 0, 0, 2, 0, 0, 0],
                                                        [0, 1, 1, 2, 1, 0, 0]])
        
    def test_minimax_voittaa_tilanteessa_4(self):
        self.peli.poyta.set_poyta([ [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 2, 2, 0, 0],
                                    [0, 0, 2, 1, 1, 1, 0]])
        self.peli.AI_peliliike()
        self.peli.pelisiirto(5)
        self.peli.AI_peliliike()
        self.peli.pelisiirto(5)
        self.peli.AI_peliliike()
        self.assertEqual(self.peli.poyta.get_poyta(), [[0, 0, 0, 0, 0, 0, 0],
                                                       [0, 0, 0, 0, 0, 0, 0],
                                                       [0, 0, 0, 0, 0, 2, 0],
                                                       [0, 0, 0, 0, 2, 1, 0],
                                                       [0, 0, 0, 2, 2, 1, 0],
                                                       [0, 0, 2, 1, 1, 1, 2]])
    
    def test_minimax_voittaa_tilanteessa_5(self):
        self.peli.poyta.set_poyta([[0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 2, 0, 0, 0],
                                   [0, 2, 2, 2, 1, 0, 0],
                                   [0, 2, 1, 1, 2, 0, 0]])
        self.peli.AI_peliliike()
        self.peli.pelisiirto(0)
        self.peli.AI_peliliike()
        self.peli.pelisiirto(1)
        self.peli.AI_peliliike()
        self.peli.pelisiirto(0)
        self.peli.AI_peliliike()
        self.peli.pelisiirto(4)
        self.peli.AI_peliliike()
        self.peli.pelisiirto(3)
        self.peli.AI_peliliike()
        self.peli.pelisiirto(2)
        self.peli.AI_peliliike()
        self.peli.pelisiirto(1)
        self.peli.AI_peliliike()
        self.assertEqual(self.peli.poyta.get_poyta(), [[2, 0, 0, 0, 0, 0, 0],
                                                       [2, 1, 1, 0, 0, 0, 0],
                                                       [2, 1, 2, 1, 2, 0, 0],
                                                       [1, 2, 2, 2, 1, 0, 0],
                                                       [1, 2, 2, 2, 1, 0, 0],
                                                       [2, 2, 1, 1, 2, 0, 0]])