![Kattavuusraportti](https://github.com/BigJackz/connect4/blob/master/Dokumentit/final%20testikattavuus%2023.3.2023.png)  
Yksikkötestaus toteutettu laajasti.  
Minimaxin testaukseen käytetyt testit löytyvät test_minimax.py tiedostosta  
Minimaxin testaukseen käytetyt tilanteet, jossa 1 viittaa pelaajan laattaan, 2 ai:n laattaan ja 0 tyhjään kohtaan, minimaxia kutsutaan syvyydellä 6 testeissä:  
Tilanteen 1 alkutilanne:  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 1]  
[0, 1, 0, 2, 2, 0, 1]  
josta kahden ai_peliliike kutsun jälkeen päästään tilanteeseen  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 1]  
[0, 1, 2, 2, 2, 2, 1]  
josta ai voittaa.  
  
Tilanteen 2 alkutilanne:  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 1]  
[0, 0, 0, 0, 2, 1, 1]  
[0, 0, 1, 2, 1, 1, 1]  
josta kahden ai_peliliike kutsun jälkeen päästään tilanteeseen  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 2]  
[0, 0, 0, 0, 0, 2, 1]  
[0, 0, 0, 0, 2, 1, 1]  
[0, 0, 1, 2, 1, 1, 1]  
josta ai voittaa.  
  
Tilanteen 3 alkutilanne:  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 2, 0, 0, 0]  
[0, 1, 1, 2, 1, 0, 0]  
josta kahden ai_peliliike kutsun jälkeen päästään tilanteeseen  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 2, 0, 0, 0]  
[0, 0, 0, 2, 0, 0, 0]  
[0, 0, 0, 2, 0, 0, 0]  
[0, 1, 1, 2, 1, 0, 0]  
josta ai voittaa.  
  
Tilanteen 4 alkutilanne:
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 2, 2, 0, 0]  
[0, 0, 2, 1, 1, 1, 0]  
josta muutamien ai:n ja pelaajan siirtojen jälkeen päästään lopputilanteeseen:
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 2, 0]  
[0, 0, 0, 0, 2, 1, 0]  
[0, 0, 0, 2, 2, 1, 0]  
[0, 0, 2, 1, 1, 1, 2]  
josta ai voittaa.  
  
Tilanteen 5 alkutilanne:  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 2, 0, 0, 0]  
[0, 2, 2, 2, 1, 0, 0]  
[0, 2, 1, 1, 2, 0, 0]  
  
monen ai:n ja pelaajan siirron jälkeen ai löytää lopulta voiton, mutta jostain syystä pitkittää peliä turhaan.  
Lopputilanne:  
[2, 0, 0, 0, 0, 0, 0]  
[2, 1, 1, 0, 0, 0, 0]  
[2, 1, 2, 1, 2, 0, 0]  
[1, 2, 2, 2, 1, 0, 0]  
[1, 2, 2, 2, 1, 0, 0]  
[2, 2, 1, 1, 2, 0, 0]  
josta ai voittaa.  
  
Lisäksi testattu, että minimax löytää voiton 4 siirrolla tyhjällä pöydällä.  
















