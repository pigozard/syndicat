#!/usr/bin/env python3
"""
Outil de la maquette CGT Perrens — à lancer depuis la racine du projet :

    python3 outils/build.py

Il fait deux choses :

1. Recopie les widgets partagés (partials/nav.html, partials/bandeau-aide.html)
   dans toutes les pages .html, et allume le bon onglet du menu.
   → On ne modifie la navigation qu'à UN endroit : partials/nav.html.

2. Génère le dossier jimdo/ : un fichier .md par page, avec chaque widget
   numéroté, prêt à copier-coller dans un « Élément HTML » Jimdo.
   Les liens sont convertis en URLs Jimdo et les images en repères [IMG:nom].

Aucune dépendance : Python 3 suffit.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Les pages du site, dans l'ordre de migration.
#   fichier     : fichier de la maquette
#   menu        : onglet du menu à allumer (data-nav dans partials/nav.html)
#   jimdo       : URL de la page sur Jimdo → À AJUSTER si Jimdo donne d'autres URLs
#   titre       : nom de la page dans Jimdo
# ---------------------------------------------------------------------------
PAGES = [
    ("index.html",            "accueil",     "/",                    "Accueil"),
    ("droits.html",           "droits",      "/droits",              "Vos droits"),
    ("droit-conges.html",     "droits",      "/droit-conges",        "Congés maladie"),
    ("droit-cgos.html",       "droits",      "/droit-cgos",          "CGOS"),
    ("droit-harcelement.html","droits",      "/droit-harcelement",   "Harcèlement"),
    ("droit-absence.html",    "droits",      "/droit-absence",       "Autorisations d'absence"),
    ("droit-rqth.html",       "droits",      "/droit-rqth",          "RQTH"),
    ("droit-syndical.html",   "droits",      "/droit-syndical",      "Droit syndical"),
    ("droit-salaires.html",   "droits",      "/droit-salaires",      "Grilles de salaires"),
    ("droit-travail.html",    "droits",      "/droit-travail",       "Temps de travail"),
    ("droit-retraite.html",   "droits",      "/droit-retraite",      "Retraite (CNRACL)"),
    ("droit-mutuelle.html",   "droits",      "/droit-mutuelle",      "Mutuelle / PSC"),
    ("droit-greve.html",      "droits",      "/droit-greve",         "Droit de grève"),
    ("droit-fei.html",        "droits",      "/droit-fei",           "Événements indésirables"),
    ("droit-elections.html",  "droits",      "/droit-elections",     "Élections professionnelles"),
    ("equipe.html",           "equipe",      "/equipe",              "L'équipe"),
    ("histoire.html",         "equipe",      "/histoire",            "La CGT expliquée"),
    ("communiques.html",      "communiques", "/communiques",         "Communiqués"),
    ("contact.html",          "contact",     "/contact",             "Contact"),
    ("adherer.html",          "",            "/adherer",             "Adhérer"),
]

# Widgets partagés : nom dans le repère WIDGET  →  fichier source
PARTIALS = {
    "Navigation": "partials/nav.html",
    "Bandeau d'aide": "partials/bandeau-aide.html",
}

WIDGET_RE = re.compile(
    r"<!-- ===== WIDGET : (?P<name>.*?) ===== -->\n(?P<body>.*?)<!-- ===== FIN WIDGET ===== -->",
    re.S,
)


def inject_partials(html, menu_key):
    for name, path in PARTIALS.items():
        part = (ROOT / path).read_text(encoding="utf-8").rstrip("\n")
        if name == "Navigation" and menu_key:
            part = part.replace(f'data-nav="{menu_key}"', f'data-nav="{menu_key}" class="active"')
        pattern = re.compile(
            r"(<!-- ===== WIDGET : " + re.escape(name) + r" ===== -->\n).*?(<!-- ===== FIN WIDGET ===== -->)",
            re.S,
        )
        if not pattern.search(html):
            raise SystemExit(f"Repère « WIDGET : {name} » introuvable")
        html = pattern.sub(lambda m: m.group(1) + part + "\n" + m.group(2), html, count=1)
    return html


def to_jimdo(body, url_of):
    """Convertit liens et images de la maquette vers Jimdo."""
    def link(m):
        target, anchor = m.group(1), m.group(2) or ""
        return f'href="{url_of.get(target, target)}{anchor}"'
    body = re.sub(r'href="([\w-]+\.html)(#[\w-]+)?"', link, body)
    body = re.sub(r'images/([\w.-]+?)\.(?:jpg|jpeg|png|svg|webp)', r"[IMG:\1]", body)
    body = re.sub(r'pdfs/([\w.-]+?)\.pdf', r"[PDF:\1]", body)
    return body


def export_page(num, file, jimdo_url, titre, html, url_of):
    widgets = [(m["name"], m["body"].strip("\n")) for m in WIDGET_RE.finditer(html)]
    title = re.search(r"<title>(.*?)</title>", html).group(1)
    out = [f"# {num:02d} — {titre}", "",
           f"**URL Jimdo :** `{jimdo_url}`  ",
           f"**Titre de la page :** `{title}`  ",
           f"**Maquette :** `{file}`", ""]

    all_widgets = "\n".join(body for _, body in widgets)
    medias = sorted(set(re.findall(r"\[(?:IMG|PDF):[\w.-]+\]", to_jimdo(all_widgets, url_of))))
    if medias:
        out += ["**Fichiers à uploader avant de coller :** " + ", ".join(f"`{m}`" for m in medias), ""]

    out += ["| # | Widget |", "|---|---|"]
    out += [f"| {i} | {name} |" for i, (name, _) in enumerate(widgets)]
    out.append("")
    for i, (name, body) in enumerate(widgets):
        out += ["---", "", f"## Widget {i} — {name}", "",
                "Jimdo : **+ → Élément HTML** → coller → Enregistrer", "",
                "```html", to_jimdo(body, url_of), "```", ""]
    return "\n".join(out), len(widgets)


def main():
    url_of = {f: u for f, _, u, _ in PAGES}
    out_dir = ROOT / "jimdo"
    out_dir.mkdir(exist_ok=True)
    for old in out_dir.glob("[0-9][0-9]-*.md"):
        old.unlink()

    for num, (file, menu, jimdo_url, titre) in enumerate(PAGES, start=1):
        path = ROOT / file
        html = inject_partials(path.read_text(encoding="utf-8"), menu)
        path.write_text(html, encoding="utf-8")

        md, n = export_page(num, file, jimdo_url, titre, html, url_of)
        (out_dir / f"{num:02d}-{Path(file).stem}.md").write_text(md, encoding="utf-8")
        print(f"  {file:<24} {n:>2} widgets  →  jimdo/{num:02d}-{Path(file).stem}.md")

    print("\nOK — pages mises à jour et dossier jimdo/ régénéré.")


if __name__ == "__main__":
    main()
