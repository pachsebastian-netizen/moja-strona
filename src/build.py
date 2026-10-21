"""Buduje statyczną stronę AllPass w trzech językach.
Użycie: python3 build.py live|preview
  live    -> ../docs     (strona publikowana przez GitHub Pages; czcionki z fonts.bunny.net)
  preview -> ./preview   (podgląd z Google Fonts, nie trafia do repozytorium)
"""
import json, shutil, sys, datetime, pathlib
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup
import content, privacy_content
from content_extra import ADDS

# ---------------- USTAWIENIA DO UZUPEŁNIENIA ----------------
# Adres formularza z Formspree, np. "https://formspree.io/f/abcdwxyz".
# Pusty = formularz otwiera program pocztowy (tryb awaryjny).
FORM_ENDPOINT = ""

PLACEHOLDER = '<span class="placeholder">{}</span>'
COMPANY = dict(
    name="AllPass Training " + PLACEHOLDER.format("[forma prawna, imię i nazwisko właściciela]"),
    address=PLACEHOLDER.format("ul. XXXXX, XX-XXX XXXXX"),
    nip=PLACEHOLDER.format("XXXXXXXXXX"),
    register="",          # dla spółki: "KRS 0000000000, Sąd Rejonowy ..., kapitał zakładowy ... zł"
    email="biuro@allpass.pl",
    phone=PLACEHOLDER.format("+48 XXX XXX XXX"),
)
POLICY_DATE = "21.10.2026"
# ------------------------------------------------------------

mode = sys.argv[1] if len(sys.argv) > 1 else "live"
base = pathlib.Path(__file__).parent
out = (base.parent / "docs") if mode == "live" else (base / "preview")
SITE_URL = "https://allpass.pl"

FAMILIES = "Unbounded:wght@400;500;600&family=Onest:wght@400;500;600"
if mode == "live":
    fonts = ('<link rel="preconnect" href="https://fonts.bunny.net">\n'
             '<link rel="stylesheet" href="https://fonts.bunny.net/css2?family=' + FAMILIES + '&display=swap">')
else:
    fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=' + FAMILIES + '&display=swap">')

PHOTOS = {"wozki": "kurs-wozki.webp", "teleskopowe": "kurs-teleskopowe.webp", "podesty": "kurs-podesty.webp", "bhp": "kurs-bhp.webp"}

LANGS = [
    dict(code="pl", hreflang="pl", short="PL", name="Polski", home="", privacy="polityka-prywatnosci/", t=content.PL, p=privacy_content.PL, x=ADDS["PL"]),
    dict(code="en", hreflang="en", short="EN", name="English", home="en/", privacy="en/privacy-policy/", t=content.EN, p=privacy_content.EN, x=ADDS["EN"]),
    dict(code="uk", hreflang="uk", short="UA", name="Українська", home="uk/", privacy="uk/privacy-policy/", t=content.UK, p=privacy_content.UK, x=ADDS["UK"]),
]

env = Environment(loader=FileSystemLoader(base / "templates"), autoescape=True)
sprite = (base / "templates/sprite.svg").read_text()
company = {k: Markup(v) for k, v in COMPANY.items()}
plain = {k: Markup(v).striptags() for k, v in COMPANY.items()}

if mode != "live":
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(base.parent / "docs/assets", out / "assets")
    shutil.copy(base.parent / "docs/favicon.png", out / "favicon.png")


def prep(l):
    t = dict(l["t"])
    t["f_hint"] = l["x"]["f_hint"]
    t["form"] = {**t["form"], **l["x"]["form_add"]}
    courses = []
    for c in t["courses"]:
        c = dict(c)
        c["from"] = c.pop("from_", False)
        c.setdefault("note", t["note_udt"])
        c.setdefault("vb", 120)
        if c["id"] in PHOTOS:
            c["photo"] = PHOTOS[c["id"]]
            c["alt"] = t["alts"][c["id"]]
        courses.append(c)
    t["courses"] = courses
    return t


def fill(s):
    return s.format(company=plain["name"], address=plain["address"], nip=plain["nip"], email=plain["email"], date=POLICY_DATE)


for l in LANGS:
    t = prep(l)
    for kind in ("home", "privacy"):
        rel_path = l[kind]                      # np. "en/privacy-policy/"
        depth = rel_path.count("/")
        root = "../" * depth
        langs = [dict(x, alt_rel=(x[kind] or "./"), alt_path="/" + x[kind]) for x in LANGS]
        common = dict(
            lang=l["code"], t=t, langs=langs, root=root, path="/" + rel_path, site_url=SITE_URL,
            fonts=fonts, sprite=sprite, year=datetime.date.today().year, company=company,
            privacy_rel=l["privacy"], home=(l["home"] or "./"),
            form_js=json.dumps(t["form"], ensure_ascii=False), form_endpoint=FORM_ENDPOINT,
        )
        if kind == "home":
            html = env.get_template("index.html").render(
                page_title=t["meta_title"], page_desc=t["meta_desc"], nav_base="", **common)
        else:
            p = l["p"]
            p = dict(p, updated=fill(p["updated"]), intro=fill(p["intro"]),
                     sections=[(h, [fill(x) for x in paras]) for h, paras in p["sections"]])
            html = env.get_template("privacy.html").render(
                page_title=f'{p["title"]} | AllPass Training', page_desc=p["meta_desc"], p=p,
                nav_base=root + (l["home"] or "./"), **common)
        target = out / rel_path / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html)
        print("built", target)

if mode == "live":
    # Plik CNAME (allpass.pl) dodamy dopiero przy podłączaniu domeny.
    (out / ".nojekyll").write_text("")
    (out / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://allpass.pl/sitemap.xml\n")
    urls = "".join(f"  <url><loc>{SITE_URL}/{l[k]}</loc></url>\n" for l in LANGS for k in ("home", "privacy"))
    (out / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
