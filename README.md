# Palautesovellus

Sovelluksesta tulee palautesovellus, jolla voi antaa palautetta oman ryhmän jäsenille. Tällä hetkellä sovelluksessa voi luoda tunnuksen ja kirjautua sisään ja ulos, sekä luoda ryhmän. Ryhmien nimet näkyvät kirjautuneille käyttäjille linkkeinä etusivulla. Ryhmien nimiä klikkaamalla ei pääse tällä hetkellä vielä minnekään.

## Sovelluksen ominaisuuksia:
Toteutetut ominaisuudet on merkitty listaan.
- [x] Käyttäjä voi luoda itselleen tunnuksen.
- [x] Käyttäjä voi kirjautua sisään ja ulos.
- [x] Käyttäjä voi luoda uuden ryhmän.
- [ ] Käyttäjä voi valita ryhmän, mihin kuuluu.
- [ ] Käyttäjä näkee sovelluksen etusivulla listan muista käyttäjistä, jotka kuuluvat samaan ryhmään.
- [ ] Käyttäjä voi kirjoittaa anonyymin viestin toiselle samaan ryhmään kuuluvalle käyttäjälle.
- [ ] Käyttäjä voi poistaa lähettämänsä viestin.
- [ ] Käyttäjä näkee listassa eri värillä ne henkilöt, joille hän on jo lähettänyt viestin.
- [ ] Käyttäjä voi lukea itselleen tulleita viestejä.


## Käyttöohjeet

Kloonaa tämä repositorio omalle koneellesi.

```
git clone git@github.com:hilliaho/palautesovellus.git
```

Siirry repositorion juurikansioon.

```
cd palautesovellus
```

Luo kansioon .env-tiedosto ja kopioi sinne seuraavat rivit:

```
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```

Aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:

```
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install flask-sqlalchemy
pip install psycopg2
pip install python-dotenv
```

Määritä tietokannan skeema komennolla:

```
psql < schema.sql
```

Sovellus käyttää tietokantatauluja nimeltä *users* ja *groups*. Jos sinulla on omassa tietokannassasi jo samannimisiä tauluja, voit seurata kurssimateriaalin ohjeita uuden tietokannan luomiseen vertaisarviointia varten.
Vaihtoehtoisesti voit myös poistaa samannimiset taulut etukäteen omasta tietokannastasi psql-komennoilla:

```
DROP TABLE users;
DROP TABLE groups;
```

Käynnistä sovellus komennolla:

```
flask run
```
