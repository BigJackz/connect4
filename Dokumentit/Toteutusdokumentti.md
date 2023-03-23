Ohjelmana on connect4 peli, jossa voi pelata joko toista pelaajaa tai tekoälyä vastaan, joka toimii minimax algoritmilla, jossa alpha beeta karsinta.

Ohjelma koostuu seitsemästä eri python tiedostosta, sekä muutamasta kuvasta. 
Ai_pisteytys.py pisteyttää eri pelitilanteita, joita minimax sitten käyttää etsiessään parasta siirtoa.
Minimax.py sisältää minimax algoritmin, jota käytetään tekoälyä vastaan pelattavassa pelissä.
Voiton_tarkastaja.py sisältää pelin voittamisen tarkastamisen logiikan.
Pelipoyta_logiikka.py vastaa pelipöydän tilanteen yllä pitämisestä, sekä muutoksien suorittamisesta pelipöydälle.
Peli_logiikka.py sisältää pelissä sisältävien arvojen ylläpitämisen, sekä niiden muuttamisen eri pelitilanteisiin sopiviksi esimerkiksi pitää tiedon pitääkö näyttää menu vai pelitilanne. Tänne on myös toteutettu sekä pelaajan, että tekoälyn siirron tekeminen.
Vuoro.py pitää yllä tietoa siitä, kumman pelaajan vuoro on ja metodit sen muokkaamiseen.
Main.py sisältää pelin graafisen käyttöliittymän piirtämisen sekä pelin käynnistämisen.