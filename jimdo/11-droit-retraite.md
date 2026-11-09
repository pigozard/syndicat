# 11 — Retraite (CNRACL)

**URL Jimdo :** `/droit-retraite`  
**Titre de la page :** `Retraite CNRACL · CGT — CH Charles Perrens`  
**Maquette :** `droit-retraite.html`

| # | Widget |
|---|---|
| 0 | Navigation |
| 1 | En-tête de page |
| 2 | Contenu de la fiche |
| 3 | Bandeau d'aide |

---

## Widget 0 — Navigation

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<header class="site-header">
  <div class="header-inner">
    <a class="logo" href="/">
      <div class="logo-mark"><span class="l1">CGT</span><span class="l2">perrens</span></div>
      <div class="logo-text"><h1>CGT — CH Charles Perrens</h1><p>Section syndicale · Fonction Publique Hospitalière</p></div>
    </a>
    <nav id="main-nav">
      <a href="/" data-nav="accueil">La CGT</a>
      <a href="/droits" data-nav="droits" class="active">Vos droits</a>
      <a href="/equipe" data-nav="equipe">L'équipe</a>
      <a href="/communiques" data-nav="communiques">Communiqués</a>
      <a href="/contact" data-nav="contact">Contact</a>
      <a href="/contact" class="nav-cta-mobile">Permanence</a>
      <a href="/adherer" class="nav-cta-mobile">Adhérer →</a>
    </nav>
    <div class="header-cta">
      <a href="/contact" class="btn btn-ghost">Permanence</a>
      <a href="/adherer" class="btn btn-red">Adhérer →</a>
    </div>
    <button class="nav-toggle" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="main-nav">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
<script>
/* Menu mobile : ouvre / ferme la liste des liens */
(function () {
  var nav = document.getElementById('main-nav');
  var btn = document.querySelector('.nav-toggle');
  if (!nav || !btn) return;
  btn.addEventListener('click', function () {
    var open = nav.classList.toggle('mobile-open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();
</script>
```

---

## Widget 1 — En-tête de page

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="droits-hero">
  <div class="droits-hero-inner">
    <a href="/droits" class="back-link">← Retour à Vos droits</a>
    <h2>👵 Retraite CNRACL</h2>
  </div>
</div>
```

---

## Widget 2 — Contenu de la fiche

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap wrap--narrow wrap--pb">
  <div class="fei-block anim">
    <p>Les agents titulaires de la Fonction Publique Hospitalière cotisent à la <strong>CNRACL</strong> (Caisse Nationale de Retraites des Agents des Collectivités Locales). Deux catégories déterminent l'âge de départ : la <strong>catégorie sédentaire</strong> (âge légal comme dans le régime général) et la <strong>catégorie active</strong>, ouverte à certains métiers exposés à un risque particulier ou à des fatigues exceptionnelles (une partie des soignants, notamment en psychiatrie), qui permet un départ anticipé sous condition de durée de services actifs.</p>
    <p><strong>Ce qui compte dans le calcul :</strong> la durée d'assurance tous régimes confondus, le nombre de trimestres validés dans la catégorie active le cas échéant, et le traitement indiciaire des 6 derniers mois. Un départ avant d'avoir la durée requise entraîne une décote ; l'inverse peut ouvrir droit à une surcote.</p>
    <p><strong>Simuler sa pension :</strong> le simulateur officiel est accessible sur <em>info-retraite.fr</em> (compte retraite unique tous régimes) et sur l'espace personnel CNRACL. Le relevé de situation individuelle (RIS) permet de vérifier que tous les trimestres sont bien enregistrés.</p>
    <div class="fei-note">[À COMPLÉTER — préciser si des agents du service relèvent de la catégorie active, et les contacts RH/CNRACL de l'établissement pour lancer une demande de départ.]</div>
  </div>
</div>
```

---

## Widget 3 — Bandeau d'aide

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="cta-band">
  <h3>Si vous avez besoin d'aide, <span>notre porte vous est toujours ouverte</span> !</h3>
  <p>Syndiqué ou non, notre porte vous est toujours ouverte.<br>
  <a href="mailto:cgt@ch-perrens.fr">cgt@ch-perrens.fr</a> · 05.56.56.35.65 · 07.68.03.34.15 · <a href="https://facebook.com/CGT.Perrens" target="_blank" rel="noopener">Facebook.com/CGT.Perrens</a> · <a href="https://instagram.com/cgt.perrens" target="_blank" rel="noopener">@cgt.perrens</a></p>
</div>
```
