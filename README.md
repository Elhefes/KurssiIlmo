# KurssiIlmo

KurssiIlmo on nettiselaimen kautta toimiva sovellus, jolla käyttäjät voivat vaivattomasti luoda omia kursseja sekä ilmoittautua toisten käyttäjien järjestämille kursseille. Ohjelma on käytettävissä nettiselaimella [Herokussa](https://kurssiilmo.herokuapp.com/courses). Sovellusta pääsee kokeilemaan joko luomalla uuden käyttäjän tai kirjautumalla seuraavilla testitunnuksilla:

Käyttäjänimi  | Salasana
------------- | -------------
testi  | kayttaja


Rekisteröitymisen/kirjautumisen jälkeen käyttäjä pääsee selaamaan kurssivalikoimaa, tarkastelemaan tarkemmin kurssitietoja sekä ilmoittautumaan itselleen mieluisille kursseille. Mikäli kurssi on maksullinen, käyttäjä saa "laskun" jossa näkyy maksun saajan tilinumero sekä hinta. Kun maksu on suoritettu, kurssin perustaja voi viimeistellä ilmoittautumisen.

Kuka tahansa voi myös luoda omia kursseja. Se tapahtuu ohjelmassa erilaisella lomakkeella, johon syötetään kurssin tiedot, kuten nimi, paikka, aika sekä kurssin kuvaus ja hinta. Sovelluksen käyttäjät pystyvät myös näkemään kurssille ilmoittautuneet henkilöt.

Käyttäjä voi myös tarkastella omia ilmoittautumisiaan. Hän voi myöskin poistaa omia ilmoittautumisiaan.


## Dokumentaatio

* [Käyttöohje](https://github.com/henripalin/KurssiIlmo/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)
* [Alustava tietokantakaavio](https://github.com/henripalin/KurssiIlmo/blob/master/dokumentaatio/tietokantakaavio.png)
* [Käyttötapaukset](https://github.com/henripalin/KurssiIlmo/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6tapaukset.md)

## Ohjelman asennus omalle tietokoneelle

Mikäli haluat ajaa sovellusta omalla laitteellasi, täytyy ensiksi kloonata repositorio. Tämän jälkeen navigoi komentorivillä _cd_-komennolla repositorion sijaintiin.

Seuraavaksi täytyy ajaa seuraavat komennot:

```python3 -m venv venv```

```pip install -r requirements.txt```

Tämä komento asentaa tarvittavat ohjelman tarvitsemat riippuvuudet. Nyt pääset ajamaan ohjelmaa komennoilla

```source venv/bin/activate```

```python run.py```

Ohjelmaa voi kokeilla osoitteessa _localhost:5000_.

## Puuttuvat/suunnitellut ominaisuudet:

* Laskutus
  * Kurssille ilmoittautumisen jälkeen käyttäjä voi tarkastella aukinaisia laskujansa. Kurssin pitäjä voi "viimeistellä" ilmoittautumisen kun maksu on toteutunut
* Kurssilistauksen järjestäminen eri kriteereillä
  
