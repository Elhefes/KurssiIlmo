## Ohjelman asennus omalle tietokoneelle

Mikäli haluat ajaa sovellusta omalla laitteellasi, täytyy ensiksi kloonata repositorio. Tämän jälkeen navigoi komentorivillä _cd_-komennolla repositorion sijaintiin.

Seuraavaksi täytyy ajaa seuraavat komennot:

```python3 -m venv venv```

```pip install -r requirements.txt```

```source venv/bin/activate```

Tämä komento asentaa tarvittavat ohjelman tarvitsemat riippuvuudet. Nyt pääset ajamaan ohjelmaa komennoilla

```python run.py```

Tämän jälkeen ohjelmaa pääsee kokeilemaan osoitteessa _localhost:5000_.

## Ohjelman siirtäminen Herokuun

Ensiksi täytyy luoda tunnukset Herokuun ja asentaa [HEROKU CLI](https://devcenter.heroku.com/articles/heroku-cli). Tämän jälkeen luodaan sovellukselle paikka Herokussa komennolla

```heroku create sovelluksen-nimi```

Lisätään vielä sovellukseen tieto siitä, että se on Herokussa. Tämä saadaan komennolla

```heroku config:set HEROKU=1```
