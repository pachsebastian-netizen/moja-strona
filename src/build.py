"""Buduje statyczną stronę AllPass w trzech językach.
Użycie: python3 build.py live|preview
  live    -> ../docs     (strona publikowana przez GitHub Pages; czcionki z fonts.bunny.net)
  preview -> ./preview   (podgląd z Google Fonts, nie trafia do repozytorium)
"""
import json, shutil, sys, datetime, pathlib
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup
import content, privacy_content, courses_content
from content_extra import ADDS

# ---------------- USTAWIENIA DO UZUPEŁNIENIA ----------------
# Adres formularza z Formspree, np. "https://formspree.io/f/abcdwxyz".
# Pusty = formularz otwiera program pocztowy (tryb awaryjny).
FORM_ENDPOINT = "https://formspree.io/f/myekrpoy"

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
# Pływający przycisk „Zadzwoń” pojawia się sam, gdy w COMPANY wpiszesz prawdziwy numer w polu phone.
CALL_LABEL = {"pl": "Zadzwoń", "en": "Call us", "uk": "Зателефонувати"}
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

PHOTOS = {}   # zdjęcia wyłączone: karty kursów pokazują ilustracje

LANGS = [
    dict(code="pl", hreflang="pl", short="PL", name="Polski", home="", privacy="polityka-prywatnosci/", t=content.PL, p=privacy_content.PL, x=ADDS["PL"], cc=courses_content.PL, ui=courses_content.UI["PL"]),
    dict(code="en", hreflang="en", short="EN", name="English", home="en/", privacy="en/privacy-policy/", t=content.EN, p=privacy_content.EN, x=ADDS["EN"], cc=courses_content.EN, ui=courses_content.UI["EN"]),
    dict(code="uk", hreflang="uk", short="UA", name="Українська", home="uk/", privacy="uk/privacy-policy/", t=content.UK, p=privacy_content.UK, x=ADDS["UK"], cc=courses_content.UK, ui=courses_content.UI["UK"]),
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


def is_set_phone(v):
    return bool(v) and "X" not in v


tel = ""
if is_set_phone(plain["phone"]):
    tel = "+" + "".join(ch for ch in plain["phone"] if ch.isdigit()) if plain["phone"].strip().startswith("+") \
        else "+48" + "".join(ch for ch in plain["phone"] if ch.isdigit())


def prep(l):
    t = dict(l["t"])
    t["f_hint"] = l["x"]["f_hint"]
    t["form"] = {**t["form"], **l["x"]["form_add"]}
    cc = l["cc"]
    courses = []
    for c in t["courses"]:
        c = dict(c)
        c["from"] = c.pop("from_", False)
        c.setdefault("note", t["note_udt"])
        c.setdefault("vb", 120)
        if c["id"] in PHOTOS:
            c["photo"] = PHOTOS[c["id"]]
            c["alt"] = t["alts"][c["id"]]
        c["slug"] = cc[c["id"]]["slug"] if c["id"] in cc else ""
        courses.append(c)
    t["courses"] = courses
    return t


def fill(s):
    return s.format(company=plain["name"], address=plain["address"], nip=plain["nip"], email=plain["email"], date=POLICY_DATE)


def is_set(v):
    return "XXX" not in v and "[" not in v


ORG_ID = SITE_URL + "/#organizacja"
REGIONS = ["Województwo śląskie", "Województwo małopolskie", "Województwo podkarpackie", "Polska"]


def org_ld(t):
    org = {
        "@type": ["EducationalOrganization", "LocalBusiness"],
        "@id": ORG_ID,
        "name": "AllPass Training",
        "url": SITE_URL + "/",
        "logo": SITE_URL + "/assets/logo-full.png",
        "image": SITE_URL + "/assets/og-image.jpg",
        "email": plain["email"],
        "description": t["meta_desc"],
        "areaServed": [{"@type": "AdministrativeArea", "name": r} for r in REGIONS],
        "knowsLanguage": ["pl", "en", "uk"],
        "priceRange": "99–1290 zł",
        "currenciesAccepted": "PLN",
    }
    if is_set(plain["phone"]):
        org["telephone"] = plain["phone"]
    if is_set(plain["address"]):
        org["address"] = {"@type": "PostalAddress", "streetAddress": plain["address"], "addressCountry": "PL"}
    if is_set(plain["nip"]):
        org["taxID"] = plain["nip"]
    return org


def course_ld(c, cc, url, lang):
    price = c["price"]
    return {
        "@type": "Course",
        "@id": url + "#kurs",
        "name": cc["h1"],
        "description": cc["desc"],
        "url": url,
        "image": SITE_URL + "/assets/og-image.jpg",
        "inLanguage": lang,
        "availableLanguage": ["pl", "en", "uk"],
        "provider": {"@id": ORG_ID},
        "educationalCredentialAwarded": "Zaświadczenie kwalifikacyjne UDT" if c["issuer"] == "UDT" else "Zaświadczenie o ukończeniu szkolenia BHP",
        "offers": {"@type": "Offer", "category": "Paid", "price": price, "priceCurrency": "PLN",
                   "url": url, "availability": "https://schema.org/InStock"},
        "hasCourseInstance": [{"@type": "CourseInstance", "courseMode": "Onsite",
                               "location": {"@type": "AdministrativeArea", "name": "Polska"}}],
    }


def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def ld(graph):
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)


pages = []   # (url, {hreflang: url}) do sitemap

for l in LANGS:
    t = prep(l)
    ui = l["ui"]
    cc_all = l["cc"]
    kinds = ["home", "privacy"] + list(cc_all.keys())
    for kind in kinds:
        is_course = kind in cc_all
        slug_of = (lambda x: x["cc"][kind]["slug"]) if is_course else (lambda x: x[kind])
        rel_path = slug_of(l)
        depth = rel_path.count("/")
        root = "../" * depth
        langs = [dict(x, alt_rel=(slug_of(x) or "./"), alt_path="/" + slug_of(x)) for x in LANGS]
        url = SITE_URL + "/" + rel_path
        home_url = SITE_URL + "/" + l["home"]
        pages.append((url, {x["hreflang"]: SITE_URL + x["alt_path"] for x in langs}))
        common = dict(
            lang=l["code"], t=t, ui=ui, langs=langs, root=root, path="/" + rel_path, site_url=SITE_URL,
            fonts=fonts, sprite=sprite, year=datetime.date.today().year, company=company,
            privacy_rel=l["privacy"], home=(l["home"] or "./"),
            form_js=json.dumps(t["form"], ensure_ascii=False), form_endpoint=FORM_ENDPOINT,
            og_image=SITE_URL + "/assets/og-image.jpg", og_w=1200, og_h=630, og_alt="AllPass Training",
            preload="",
            tel=tel, call_label=CALL_LABEL[l["code"]],
        )
        if kind == "home":
            graph = [{"@type": "WebSite", "@id": SITE_URL + "/#strona", "url": home_url, "name": "AllPass Training",
                      "inLanguage": l["code"], "publisher": {"@id": ORG_ID}},
                     org_ld(t),
                     {"@type": "ItemList", "name": t["courses_h2"], "itemListElement": [
                         {"@type": "ListItem", "position": i + 1, "url": SITE_URL + "/" + c["slug"]}
                         for i, c in enumerate([c for c in t["courses"] if c["slug"]])]}]
            common.update(hero_svg=env.from_string((base / "templates/hero.svg").read_text()).render(t=t))
            html = env.get_template("index.html").render(
                page_title=t["meta_title"], page_desc=t["meta_desc"], nav_base="", jsonld=ld(graph), **common)
        elif kind == "privacy":
            p = l["p"]
            p = dict(p, updated=fill(p["updated"]), intro=fill(p["intro"]),
                     sections=[(h, [fill(x) for x in paras]) for h, paras in p["sections"]])
            graph = [org_ld(t), crumbs_ld([(ui["crumb_home"], home_url), (p["title"], url)])]
            html = env.get_template("privacy.html").render(
                page_title=f'{p["title"]} | AllPass Training', page_desc=p["meta_desc"], p=p,
                nav_base=root + (l["home"] or "./"), jsonld=ld(graph), **common)
        else:
            c = next(x for x in t["courses"] if x["id"] == kind)
            cc = cc_all[kind]
            others = [x for x in t["courses"] if x["slug"] and x["id"] != kind]
            graph = [org_ld(t), course_ld(c, cc, url, l["code"]),
                     crumbs_ld([(ui["crumb_home"], home_url), (ui["crumb_courses"], home_url + "#kursy"), (c["name"], url)])]
            html = env.get_template("course.html").render(
                page_title=cc["title"], page_desc=cc["desc"], c=c, cc=cc, others=others,
                nav_base=root + (l["home"] or "./"), jsonld=ld(graph), **common)
        target = out / rel_path / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html)
        print("built", target)

if mode == "live":
    (out / "CNAME").write_text("allpass.pl\n")  # domena podłączona w GitHub Pages
    (out / ".nojekyll").write_text("")
    (out / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: https://allpass.pl/sitemap.xml\n")
    today = datetime.date.today().isoformat()
    rows = []
    for u, alts in pages:
        links = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{h}" href="{a}"/>' for h, a in alts.items())
        rows.append(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{today}</lastmod>{links}\n  </url>")
    (out / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(rows) + "\n</urlset>\n")
