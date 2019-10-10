## Ohjelman asennus omalle tietokoneelle

Mikäli haluat ajaa sovellusta omalla laitteellasi, täytyy ensiksi kloonata repositorio. Tämän jälkeen navigoi komentorivillä _cd_-komennolla repositorion sijaintiin.

Seuraavaksi täytyy ajaa seuraavat komennot:

```python3 -m venv venv```

```pip install -r requirements.txt```

Tämä komento asentaa tarvittavat ohjelman tarvitsemat riippuvuudet. Nyt pääset ajamaan ohjelmaa komennoilla

```source venv/bin/activate```

```python run.py```

Ohjelmaa voi kokeilla osoitteessa _localhost:5000_.
