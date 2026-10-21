#!/usr/bin/env python3
"""Génère les pages HTML du site Alban Vayer Paysagiste (maquette).
Usage : python3 outils/build.py   (depuis la racine du dépôt)"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://webaunet.github.io/alban-vayer-paysagiste/"
TEL = "06 12 33 76 09"
TELHREF = "tel:+33612337609"
MAIL = "alban.vayer@gmail.com"
MAILTO = "mailto:%s?subject=Demande%%20pour%%20mon%%20jardin" % MAIL

MENU = [("index.html", "Accueil"), ("prestations.html", "Prestations"),
        ("realisations.html", "Réalisations"), ("contact.html", "Contact")]


def head(title, desc, extra_js=""):
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Source+Sans+3:wght@400;600;700&display=swap">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
""" % (title, desc)


def header(current):
    links = []
    for href, label in MENU:
        cur = ' aria-current="page"' if href == current else ""
        links.append('      <a href="%s"%s>%s</a>' % (href, cur, label))
    return """<header class="site-header" id="top">
  <div class="wrap head-in">
    <a class="logo" href="%s" aria-label="Alban Vayer Paysagiste, accueil"><b>Alban Vayer</b><span>Paysagiste</span></a>
    <nav class="nav" id="menu" aria-label="Navigation principale">
%s
    </nav>
    <a class="btn btn-primary head-cta" href="%s" aria-label="Appeler le %s"><span class="long">%s</span><span aria-hidden="true" class="short">Appeler</span></a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="menu" aria-label="Ouvrir le menu">
      <svg class="b" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      <svg class="x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
  </div>
</header>
<main>
""" % (BASE, "\n".join(links), TELHREF, TEL, TEL)


FOOTER = """</main>
<footer class="site-footer">
  <div class="wrap foot-in">
    <span><strong>Alban Vayer Paysagiste</strong> · Beynes (78)</span>
    <nav class="foot-nav" aria-label="Pied de page"><a href="prestations.html">Prestations</a><a href="realisations.html">Réalisations</a><a href="contact.html">Contact</a><a href="mentions-legales.html">Mentions légales</a></nav>
    <span><a href="%s">%s</a><a href="mailto:%s">%s</a></span>
  </div>
</footer>
""" % (TELHREF, TEL, MAIL, MAIL)


def page(name, title, desc, current, body, js=()):
    scripts = "".join('<script src="js/%s"></script>\n' % j for j in ("main.js",) + tuple(js))
    html = head(title, desc) + header(current) + body + FOOTER + scripts + "</body>\n</html>\n"
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)


# ---------- ACCUEIL ----------
home = open(os.path.join(ROOT, "outils", "home-main.html"), encoding="utf-8").read()
page("index.html",
     "Alban Vayer Paysagiste à Beynes (78) | Création et entretien de jardins",
     "Alban Vayer, paysagiste à Beynes (78) : création et entretien d'espaces verts, arrosage automatique. Appelez le 06 12 33 76 09.",
     "index.html", home)

# ---------- PRESTATIONS ----------
SEASON_ICONS = {
    "print": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><circle cx="24" cy="24" r="4"/><circle cx="24" cy="11" r="5"/><circle cx="24" cy="37" r="5"/><circle cx="11" cy="24" r="5"/><circle cx="37" cy="24" r="5"/></svg>',
    "ete": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><circle cx="24" cy="24" r="8"/><path d="M24 5v6M24 37v6M5 24h6M37 24h6M10 10l4 4M34 34l4 4M38 10l-4 4M14 34l-4 4"/></svg>',
    "aut": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M40 8C16 8 8 20 8 30c0 4 3 8 8 8 12 0 24-8 24-30z"/><path d="M8 40L26 22"/></svg>',
    "hiv": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M24 5v38M7.5 14.5l33 19M40.5 14.5l-33 19M18 7l6 5 6-5M18 41l6-5 6 5"/></svg>',
}

prest = """  <section class="page-head" aria-labelledby="h1">
    <div class="wrap ph-grid">
      <div>
        <p class="eyebrow">Prestations</p>
        <h1 id="h1">Créer, entretenir, arroser</h1>
        <p class="lead">Trois prestations réunies chez Alban Vayer, paysagiste à Beynes : création d'espaces verts, entretien et arrosage automatique.</p>
        <div class="actions">
          <a class="btn btn-primary" href="#creation">Créer</a>
          <a class="btn btn-dark" href="#entretien">Entretenir</a>
        </div>
      </div>
      <div class="mosaic">
        <img src="images/creation-espace-vert.jpg" width="1000" height="545" alt="Jardinière installant des plantes dans un massif courbe bordé de gravier, devant une maison moderne" fetchpriority="high">
        <img src="images/jardin-entretenu-allee.jpg" width="1000" height="545" alt="Jardin entretenu : pelouse tondue en bandes, allée de gravier et massifs fleuris devant une maison en pierre">
        <img src="images/tonte-pelouse.jpg" width="1000" height="558" alt="Jardinier tondant la pelouse devant une maison aux volets bleus">
      </div>
    </div>
  </section>

  <section class="section s-pierre" id="creation" aria-labelledby="t-creation">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Créer</p>
        <h2 class="section-title" id="t-creation">Création d'espaces verts</h2>
        <p>Un terrain à aménager, un jardin à reprendre, un coin à transformer : Alban Vayer imagine l'espace avec vous, puis le met en place.</p>
        <p>Le projet part de votre terrain, de votre maison et de la façon dont vous voulez vivre dehors.</p>
        <ul class="checks"><li>Un échange sur vos envies avant tout travail</li><li>Un jardin pensé pour votre terrain</li><li>Un interlocuteur unique, du projet à la plantation</li></ul>
      </div>
      <div class="imgs">
        <img src="images/muret-pierre-escalier.jpg" width="1000" height="545" loading="lazy" alt="Maçon paysagiste montant un muret en pierre et un escalier dans un jardin en pente">
        <img src="images/plantation-massif.jpg" width="1000" height="546" loading="lazy" alt="Jardinier plantant un arbuste dans un massif fraîchement creusé">
      </div>
    </div>
  </section>

  <section class="band" id="entretien" aria-labelledby="t-entretien">
    <div class="wrap">
      <p class="eyebrow" style="color:#cfe7b9">Entretenir</p>
      <h2 class="on-dark" id="t-entretien">Un jardin suivi au fil des saisons</h2>
      <p class="lead">L'entretien d'espaces verts, c'est un rendez-vous régulier avec votre jardin. Chaque saison a son rythme.</p>
      <div class="seasons">
        <article class="season s-print">""" + SEASON_ICONS["print"] + """<span class="when">Mars à mai</span><h3>Printemps</h3><p>Le jardin repart : c'est la saison où il demande le plus d'attention.</p></article>
        <article class="season s-ete">""" + SEASON_ICONS["ete"] + """<span class="when">Juin à août</span><h3>Été</h3><p>La chaleur s'installe, la pelouse et les massifs ont besoin d'eau.</p></article>
        <article class="season s-aut">""" + SEASON_ICONS["aut"] + """<span class="when">Septembre à novembre</span><h3>Automne</h3><p>Les feuilles tombent et les massifs se préparent pour l'hiver.</p></article>
        <article class="season s-hiv">""" + SEASON_ICONS["hiv"] + """<span class="when">Décembre à février</span><h3>Hiver</h3><p>Le jardin se repose, c'est le moment de préparer la saison suivante.</p></article>
      </div>
      <p class="lead" style="margin-top:2rem">Pour connaître le suivi proposé pour votre jardin, appelez Alban Vayer au <a href="%s" style="color:#fff;font-weight:700">%s</a>.</p>
    </div>
  </section>

  <section class="section s-blanc" id="arrosage" aria-labelledby="t-arrosage">
    <div class="wrap split rev">
      <div>
        <p class="eyebrow">Arroser</p>
        <h2 class="section-title" id="t-arrosage">Arrosage automatique</h2>
        <p>Un système d'arrosage automatique s'occupe de votre pelouse et de vos massifs à votre place, sans tuyau à dérouler.</p>
        <p>Il s'installe en même temps qu'un jardin neuf, ou dans un jardin existant.</p>
      </div>
      <div class="imgs">
        <img src="images/jardin-robot-tonte-arrosage.jpg" width="1000" height="545" loading="lazy" alt="Jardin en terrasses avec un robot de tonte sur la pelouse et un jet d'arrosage en fonctionnement">
      </div>
    </div>
  </section>

  <section class="contact" aria-labelledby="t-contact">
    <img class="bg" src="images/allee-dallee-maison-pierre.jpg" width="1200" height="655" loading="lazy" alt="Allée dallée éclairée au crépuscule devant une maison en pierre">
    <div class="wrap contact-in">
      <h2 id="t-contact">Quelle prestation pour votre jardin ?</h2>
      <p class="lead">Dites à Alban Vayer ce que vous imaginez : création, entretien ou arrosage automatique.</p>
      <div class="actions">
        <a class="btn btn-primary" href="%s">Appeler le %s</a>
        <a class="btn btn-ghost" href="contact.html">Écrire via le formulaire</a>
      </div>
    </div>
  </section>
""" % (TELHREF, TEL, TELHREF, TEL)
page("prestations.html",
     "Prestations de paysagiste à Beynes (78) | Alban Vayer",
     "Création d'espaces verts, entretien de jardin et arrosage automatique à Beynes (78) : découvrez les prestations d'Alban Vayer, paysagiste.",
     "prestations.html", prest)

# ---------- RÉALISATIONS ----------
real = """  <section class="page-head" aria-labelledby="h1">
    <div class="wrap ph-grid">
      <div>
        <p class="eyebrow">Réalisations</p>
        <h1 id="h1">Des jardins vus de près</h1>
        <p class="lead">Un aperçu des univers de jardin qu'Alban Vayer, paysagiste à Beynes, crée et entretient.</p>
        <div class="actions">
          <a class="btn btn-primary" href="#creations">Voir les créations</a>
          <a class="btn btn-dark" href="#entretiens">Voir l'entretien</a>
        </div>
      </div>
      <div class="fan" aria-label="Aperçu de photos de jardins">
        <img src="images/allee-paves-jardin.jpg" width="1408" height="768" alt="Allée dallée en pierre bordée d'un muret fleuri, menant à une maison de campagne en pierre" fetchpriority="high">
        <img src="images/etude-projet-tablette.jpg" width="1000" height="545" alt="Un paysagiste présente le plan d'un jardin sur une tablette, avec le jardin réel en arrière-plan">
        <img src="images/jardin-entretenu-allee.jpg" width="1000" height="545" alt="Jardin entretenu : pelouse tondue en bandes, allée de gravier et massifs fleuris devant une maison en pierre">
      </div>
    </div>
  </section>

  <section class="section s-pierre" id="creations" aria-labelledby="t-crea">
    <div class="wrap">
      <p class="eyebrow">Créations</p>
      <h2 class="section-title" id="t-crea">Aménager, planter, construire</h2>
      <div class="gallery3">
        <figure><img src="images/muret-pierre-escalier.jpg" width="1000" height="545" loading="lazy" alt="Maçon paysagiste montant un muret en pierre et un escalier dans un jardin en pente"><figcaption>Muret et escalier en pierre</figcaption></figure>
        <figure><img src="images/creation-espace-vert.jpg" width="1000" height="545" loading="lazy" alt="Jardinière installant des plantes dans un massif courbe bordé de gravier, devant une maison moderne"><figcaption>Massif courbe</figcaption></figure>
        <figure><img src="images/plantation-massif.jpg" width="1000" height="546" loading="lazy" alt="Jardinier plantant un arbuste dans un massif fraîchement creusé"><figcaption>Plantation</figcaption></figure>
      </div>
      <p class="note">Photos d'illustration.</p>
    </div>
  </section>

  <section class="band" id="entretiens" aria-labelledby="t-ent">
    <div class="wrap">
      <p class="eyebrow" style="color:#cfe7b9">Entretien</p>
      <h2 class="on-dark" id="t-ent">Des jardins qui gardent leur forme</h2>
      <div class="gallery3">
        <figure><img src="images/desherbage-massif.jpg" width="1000" height="546" loading="lazy" alt="Jardinier agenouillé désherbant un massif fleuri au bord d'une allée de gravier"><figcaption>Massif entretenu</figcaption></figure>
        <figure><img src="images/tonte-pelouse.jpg" width="1000" height="558" loading="lazy" alt="Jardinier tondant la pelouse devant une maison aux volets bleus"><figcaption>Pelouse tondue</figcaption></figure>
        <figure><img src="images/jardin-robot-tonte-arrosage.jpg" width="1000" height="545" loading="lazy" alt="Jardin en terrasses avec un robot de tonte sur la pelouse et un jet d'arrosage en fonctionnement"><figcaption>Jardin en terrasses</figcaption></figure>
      </div>
      <p class="lead" style="margin-top:1.5rem">Photos d'illustration.</p>
    </div>
  </section>

  <section class="contact" aria-labelledby="t-contact">
    <img class="bg" src="images/allee-dallee-maison-pierre.jpg" width="1200" height="655" loading="lazy" alt="Allée dallée éclairée au crépuscule devant une maison en pierre">
    <div class="wrap contact-in">
      <h2 id="t-contact">Votre jardin sera le prochain ?</h2>
      <p class="lead">Racontez votre projet à Alban Vayer, il vous répond directement.</p>
      <div class="actions">
        <a class="btn btn-primary" href="%s">Appeler le %s</a>
        <a class="btn btn-ghost" href="%s">Écrire un e-mail</a>
      </div>
    </div>
  </section>
""" % (TELHREF, TEL, MAILTO)
page("realisations.html",
     "Réalisations de paysagiste à Beynes (78) | Alban Vayer",
     "Aperçu de jardins créés et entretenus par Alban Vayer, paysagiste à Beynes (78) : aménagements, plantations et entretien.",
     "realisations.html", real)

# ---------- CONTACT ----------
contact = """  <section class="page-head" aria-labelledby="h1">
    <div class="wrap ph-grid">
      <div>
        <p class="eyebrow">Contact</p>
        <h1 id="h1">Parlons de votre jardin</h1>
        <p class="lead">Un appel suffit pour décrire votre projet. Vous pouvez aussi préparer votre message avec le formulaire ci-dessous.</p>
        <div class="actions">
          <a class="btn btn-primary" href="%s">Appeler le %s</a>
          <a class="btn btn-dark" href="#formulaire">Préparer mon message</a>
        </div>
      </div>
      <div class="panel">
        <img src="images/allee-paves-jardin.jpg" width="1408" height="768" alt="Allée dallée en pierre bordée d'un muret fleuri, menant à une maison de campagne en pierre" fetchpriority="high">
        <strong>Alban Vayer, paysagiste</strong>
        <a class="tel" href="%s">%s</a>
        <a class="mail" href="mailto:%s">%s</a>
        <span>Beynes (78)</span>
      </div>
    </div>
  </section>

  <section class="s-form" id="formulaire" aria-labelledby="t-form">
    <div class="wrap form-wrap">
      <div>
        <p class="eyebrow">Formulaire</p>
        <h2 class="section-title" id="t-form">Préparez votre demande</h2>
        <p class="section-intro">Ce site ne peut pas envoyer de message à votre place. Remplissez le formulaire : vous obtenez un message prêt à copier ou à envoyer par e-mail, et un bouton pour appeler.</p>
        <form class="form" id="contact-form" novalidate style="margin-top:1.8rem">
          <div class="field"><label for="nom">Nom <span class="req" aria-hidden="true">*</span></label><input id="nom" name="nom" type="text" autocomplete="name" required aria-describedby="err-nom"><p class="err" id="err-nom" role="alert"></p></div>
          <div class="field"><label for="tel">Téléphone <span class="req" aria-hidden="true">*</span></label><input id="tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" required aria-describedby="err-tel"><p class="err" id="err-tel" role="alert"></p></div>
          <div class="field"><label for="email">E-mail (facultatif)</label><input id="email" name="email" type="email" autocomplete="email" aria-describedby="err-email"><p class="err" id="err-email" role="alert"></p></div>
          <div class="field"><label for="projet">Type de demande <span class="req" aria-hidden="true">*</span></label>
            <select id="projet" name="projet" required aria-describedby="err-projet"><option value="">Choisir…</option><option>Création d'espaces verts</option><option>Entretien d'espaces verts</option><option>Arrosage automatique</option><option>Autre demande</option></select><p class="err" id="err-projet" role="alert"></p></div>
          <div class="field"><label for="message">Votre message <span class="req" aria-hidden="true">*</span></label><textarea id="message" name="message" required aria-describedby="err-message"></textarea><p class="err" id="err-message" role="alert"></p></div>
          <p class="hint"><span class="req" aria-hidden="true">*</span> Champs obligatoires</p>
          <button class="btn btn-primary" type="submit">Préparer mon message</button>
        </form>
      </div>
      <aside aria-label="Récapitulatif de la demande">
        <div class="recap" id="recap" tabindex="-1" hidden>
          <h3>Votre message est prêt</h3>
          <pre id="recap-text"></pre>
          <div class="actions">
            <button class="btn btn-primary" type="button" id="copy-btn">Copier</button>
            <a class="btn btn-ghost" href="%s">Appeler</a>
            <a class="btn btn-ghost" id="recap-mail" href="%s">Envoyer par e-mail</a>
            <button class="btn btn-ghost" type="button" id="edit-btn">Modifier</button>
          </div>
          <p class="status" id="copy-status" role="status"></p>
        </div>
        <p class="hint" style="margin-top:1rem">Votre message reste dans votre navigateur tant que vous ne l'envoyez pas vous-même.</p>
      </aside>
    </div>
  </section>
""" % (TELHREF, TEL, TELHREF, TEL, MAIL, MAIL, TELHREF, MAILTO)
page("contact.html",
     "Contact paysagiste à Beynes (78) | Alban Vayer",
     "Contactez Alban Vayer, paysagiste à Beynes (78), au 06 12 33 76 09 ou par e-mail, et préparez votre demande avec le formulaire.",
     "contact.html", contact, js=("contact.js",))

# ---------- MENTIONS LÉGALES ----------
legal = """  <section class="section s-simple" aria-labelledby="h1">
    <div class="wrap legal">
      <h1 id="h1">Mentions légales</h1>
      <p>Cette page présente les informations disponibles sur l'entreprise éditrice du site.</p>
      <h2>Entreprise</h2>
      <ul>
        <li>Nom : Alban Vayer</li>
        <li>Dirigeant (registre) : Alban Pierre Georges Vayer</li>
        <li>SIREN : 481 640 209</li>
        <li>Activité : services d'aménagement paysager</li>
        <li>Commune : Beynes (78)</li>
      </ul>
      <h2>Contact</h2>
      <ul>
        <li>Téléphone : <a href="%s">%s</a></li>
        <li>E-mail : <a href="mailto:%s">%s</a></li>
      </ul>
      <h2>Informations à compléter</h2>
      <p>Forme juridique, adresse du siège, numéro de TVA, directeur de la publication et hébergeur du site ne sont pas renseignés dans les sources disponibles. Ils seront ajoutés à la mise en ligne définitive.</p>
      <h2>Maquette</h2>
      <p>Ce site est une maquette de présentation. Les photos sont des visuels d'illustration.</p>
    </div>
  </section>
""" % (TELHREF, TEL, MAIL, MAIL)
page("mentions-legales.html",
     "Mentions légales | Alban Vayer Paysagiste à Beynes",
     "Mentions légales du site d'Alban Vayer, paysagiste à Beynes (78) : identité de l'entreprise et informations de contact.",
     "", legal)
print("pages générées")
