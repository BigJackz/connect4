### Käyttöohje

Asenna ohjelman riippuvuudet komennolla:
```poetry install```
Siirry kansioon connectfour, jonka jälkeen ohjelman voi käynnistää komennoilla:
```python main.py``` tai ```poetry run main.py``` tai ```poetry run python main.py```

Ohjelmassa navigoidaan hiiren vasenta nappia painelemalla.
Pelin laatat tippuvat lokeroon siihen kohtaan minne hiirellä klikkaa.

### Testaus

Ohjelman testit voidaan suorittaa komennolla:
```poetry run pytest connectfour```