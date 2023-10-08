# Palautesovellus

Sovelluksesta tulee palautesovellus, jolla voi antaa palautetta projektin jäsenille. 

Edellisen vertaisarviointikierroksen jälkeen sovellukseen on lisätty ominaisuudet:
- [x] Käyttäjä voi lisätä nimensä ja roolinsa projektin osallistujalistaan.
- [x] Käyttäjä näkee projektin sivulla listan projektin osallistujista.

## Sovelluksen ominaisuuksia:
Toteutetut ominaisuudet on merkitty listaan.
- [x] Käyttäjä voi luoda itselleen tunnuksen.
- [x] Käyttäjä voi kirjautua sisään ja ulos.
- [x] Käyttäjä näkee etusivulla listan projekteista. 
- [x] Käyttäjä voi luoda uuden projektin.
- [x] Käyttäjä voi lisätä nimensä ja roolinsa projektin osallistujalistaan.
- [x] Käyttäjä näkee projektin sivulla listan projektin osallistujista.
- [ ] Käyttäjä voi kirjoittaa anonyymin viestin toiselle samaan projektiin kuuluvalle käyttäjälle.
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
pip install -r requirements.txt
```

Määritä tietokannan skeema komennolla:

```
psql < schema.sql
```

Sovelluksen käyttämien tietokantataulujen nimet löydät schema.sql-tiedostosta. Jos sinulla on omassa tietokannassasi jo samannimisiä tauluja, voit seurata kurssimateriaalin ohjeita uuden tietokannan luomiseen vertaisarviointia varten.
Vaihtoehtoisesti voit myös poistaa samannimiset taulut etukäteen omasta tietokannastasi ajamalla jokaista taulua kohti psql-komennon:

```
DROP TABLE <taulun nimi>;
```

Käynnistä sovellus komennolla:

```
flask run
```
