# KurssiIlmo

KurssiIlmo on nettiselaimen kautta toimiva sovellus, jolla käyttäjät voivat vaivattomasti luoda omia kursseja sekä ilmoittautua toisten käyttäjien järjestämille kursseille. Ohjelma on käytettävissä nettiselaimella [Herokussa](https://kurssiilmo.herokuapp.com/courses). Sovellusta pääsee kokeilemaan testitunnuksilla käyttäjänimellä *testi* ja salasanalla *kayttaja*.

Käyttäjän on ensin rekisteröidyttävä sivulle, jotta hän pääsee ilmoittautumaan kursseille. Tämän jälkeen hän pääsee selaamaan kurssivalikoimaa, näkemään kurssitietoja ja valitsemaan sieltä mieleisiä kursseja. Mikäli kurssi on maksullinen, voidaan käyttäjä saa "laskun" jossa näkyy maksun saajan tilinumero sekä hinta.

Kuka tahansa voi myös luoda omia kursseja. Se tapahtuu ohjelmassa erilaisella lomakkeella, johon syötetään kurssin tiedot, kuten nimi, paikka, aika sekä kurssin kuvaus ja hinta. Järjestäjä pystyy myös tarkastelemaan kursseillensa ilmoittautuneita henkilöitä.

Käyttäjä voi myös tarkastella kursseja, joihin hän on ilmoittautunut. Hän voi myöskin poistaa omia ilmoittautumisiaan.


## Dokumentaatio

* [Käyttöohje](https://github.com/henripalin/KurssiIlmo/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)
* [Alustava tietokantakaavio](https://github.com/henripalin/KurssiIlmo/blob/master/dokumentaatio/tietokantakaavio.png)
* [Käyttötapaukset](https://github.com/henripalin/KurssiIlmo/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6tapaukset.md)

## Ohjelman asennus omalle tietokoneelle

Ensiksi sinun täytyy kloonata repositorio. Tämän jälkeen mene komentorivillä cd-komennolla repositorion sijaintiin.

Seuraavaksi täytyy ajaa seuraavat komennot:

```python3 -m venv venv```

```pip install -r requirements.txt```

Tämän jälkeen pääset ajamaan ohjelmaa komennolla

```python run.py```

Nyt pääset kokeilemaan ohjelmaa osoitteessa localhost:5000.
