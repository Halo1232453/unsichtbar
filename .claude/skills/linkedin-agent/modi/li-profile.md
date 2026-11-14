# /li-profile · Profil oder Unternehmensseite bewerten und umschreiben

Ein Profil ist kein Lebenslauf. Ein Lebenslauf beantwortet «was hast du
gemacht». Ein Profil beantwortet «soll ich dieser Person schreiben», und zwar in
etwa vier Sekunden, über die Headline und die ersten zwei Zeilen der Info. Für
eine Unternehmensseite gilt dasselbe mit Logo, Slogan und den ersten Zeilen der
Übersicht.

## Welche Rubrik

- **Persönliches Profil** (z.B. Bertan): `daten/profil-rubrik.json`
- **Unternehmensseite** (z.B. digitalONLY AG): `daten/seiten-rubrik.json`

Unklar? Fragen. Beide haben zwölf Punkte und 100 Punkte total.

## Eingabe

Den Menschen bitten, einzufügen:

- Profil: Headline, Info, aktuelle Position und die letzten zwei Stellen, dazu
  ob Titelbild und «Im Fokus» vorhanden sind.
- Seite: Slogan, Übersicht, Stammdaten, Follower-Zahl, ob Titelbild, Logo und
  angehefteter Beitrag vorhanden sind, und wann der letzte Beitrag war.

Ein Screenshot der oberen Karte reicht für den ersten Durchgang. Sich nicht im
Namen des Menschen bei LinkedIn anmelden.

## Bewerten

Rubrik lesen, jeden Punkt bewerten, Tabelle zeigen, Total nennen. Ehrlich:
Profile landen beim ersten Mal meist zwischen 30 und 49, neue Seiten oft
darunter. Eine grosszügige Note ist nutzlos.

```
SEITEN-SCORE  34/100

  Slogan                 3/12   «Ihre Digitalagentur», kein Kunde, kein Ergebnis
  Aktivität 7 Tage       0/12   noch kein Beitrag
  Übersicht, 2 Zeilen    4/10   beginnt mit dem Gründungsjahr
  Follower-Basis         2/10   unter 100
  ...
```

## Dann umschreiben, in dieser Reihenfolge

In absteigender Reihenfolge der verlorenen Punkte. Nicht alles auf einmal, der
Mensch muss jeden Teil selbst einfügen.

**Profil**

1. **Headline (220 Zeichen).** Bewährte Form: `{was du für wen tust} | {Beleg} |
   {wie man startet}`. Nicht der Jobtitel. Nicht «Ich helfe X, Y zu ...» als
   erste Wörter, so beginnt inzwischen jedes zweite Profil. Drei Varianten.
2. **Info, erste zwei Zeilen.** Alles danach ist auf dem Handy hinter «mehr
   anzeigen». Diese zwei Zeilen sind für die meisten die ganze Info. Wem helft
   ihr, was ändert sich. Kein «leidenschaftlich», kein «ergebnisorientiert», keine
   dritte Person, kein Einstieg mit dem eigenen Namen.
3. **Info, Rest.** An eine Leserin, in der zweiten Person: ihr Problem, was ihr
   dagegen tut, ein Beleg mit Zahl, der nächste Schritt. Unter 1400 Zeichen.
4. **Im Fokus.** Drei Elemente: bester Beitrag, ein Beleg, Kontaktweg. Leer sind
   das acht verschenkte Punkte und der einzige Teil, den man ganz kontrolliert.
5. **Berufserfahrung.** Pro Stelle eine Zeile Umfang und zwei bis drei
   Ergebnisse mit Zahlen, keine Aufgaben. Älter als zehn Jahre: eine Zeile.
6. **Titelbild.** Ein Satz Positionierung und ein Kontaktweg.

**Unternehmensseite**

1. **Slogan.** Wem ihr helft und was sich ändert, mit einem Suchbegriff, den die
   Kundschaft benutzt (Google Maps, Arztpraxen, Schweiz). Drei Varianten.
2. **Aktivität.** Keine Umschreibung hilft hier, nur Beiträge. Auf /li-plan
   und /li-woche verweisen.
3. **Übersicht, erste zwei Zeilen**, dann der Rest (Leistungen, Region, Beleg,
   nächster Schritt).
4. **Follower-Basis.** Konkrete Schritte: Team einladen, passende Kontakte der
   Partner einladen, Seite in E-Mail-Signatur und auf der Website verlinken.
5. **Verknüpfte Mitarbeitende, Aktions-Button, Titelbild, Stammdaten,
   angehefteter Beitrag.**

## Ausgabe

Score-Tabelle, dann die Umschreibungen als kopierfertige Blöcke in
Behebungs-Reihenfolge, jede durch `modi/li-human.md`. Am Ende neu bewerten und
den Unterschied ehrlich zeigen: Kommt die Umschreibung auf 78 und nicht 98, dann
78, und sagen, was die restlichen Punkte brauchen (meist Empfehlungen, ein echtes
Titelbild, Beitragsgeschichte, Follower, was keine Umschreibung erzeugen kann).

Nichts wird bei LinkedIn gespeichert. Der Mensch fügt jeden Abschnitt ein.
