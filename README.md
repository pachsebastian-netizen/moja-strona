# AllPass Training – strona allpass.pl

Strona firmowa: kursy UDT (wózki widłowe, ładowarki teleskopowe, podesty ruchome) i szkolenia BHP. Trzy wersje językowe: polska, angielska, ukraińska.

## Struktura

- `docs/` – gotowa strona publikowana przez GitHub Pages (gałąź `main`, folder `/docs`). Nie edytuj plików HTML ręcznie, generuje je skrypt.
- `docs/assets/` – style, logo, zdjęcia (zdjęcia: Unsplash i Pexels, licencje pozwalają na darmowe użycie komercyjne).
- `src/` – źródła:
  - `content.py` – teksty strony i cennik (PL / EN / UA),
  - `content_extra.py` – komunikaty formularza,
  - `privacy_content.py` – polityka prywatności,
  - `templates/` – szablony HTML,
  - `build.py` – generator; na górze są ustawienia: adres formularza Formspree, dane firmy, data polityki.

## Jak wprowadzić zmianę

1. Zmień tekst lub cenę w `src/content.py` (albo dane firmy w `src/build.py`).
2. Uruchom `cd src && python3 build.py live` (wymaga Pythona i pakietu `jinja2`).
3. Zatwierdź zmiany w repozytorium. GitHub Pages opublikuje stronę w ciągu 1–2 minut.

## Do uzupełnienia przed startem

- `FORM_ENDPOINT` w `src/build.py` – adres formularza z formspree.io,
- `COMPANY` w `src/build.py` – nazwa firmy, adres, NIP, telefon (dla spółki także KRS),
- plik `docs/CNAME` z treścią `allpass.pl` – dopiero przy podłączaniu domeny.
