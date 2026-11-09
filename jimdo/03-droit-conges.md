# 03 — Congés maladie

**URL Jimdo :** `/droit-conges`  
**Titre de la page :** `Congés maladie · CGT — CH Charles Perrens`  
**Maquette :** `droit-conges.html`

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
    <h2>🩺 Congés maladie</h2>
  </div>
</div>
```

---

## Widget 2 — Contenu de la fiche

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap wrap--narrow wrap--pb">
  <div class="fei-block anim">
    <p><strong>CMO — Congé de Maladie Ordinaire :</strong> jusqu'à 1 an maximum. 3 mois à 90% du salaire (avec un jour de carence) + 9 mois à demi-traitement. Certificat médical à transmettre dans les 48h.</p>
    <p><strong>CLM — Congé Longue Maladie :</strong> pour pathologies invalidantes (selon liste réglementée), jusqu'à 3 ans. 1 an à plein traitement + 2 ans à 60% du salaire.</p>
    <p><strong>CLD — Congé Longue Durée :</strong> pour maladies spécifiques (cancer, tuberculose, etc.), jusqu'à 5 ans. 3 ans à plein traitement + 2 ans à demi-traitement.</p>
    <p><strong>Accident du travail :</strong> événement soudain survenu dans le cadre du travail (le trajet domicile-travail peut être inclus). Délai de déclaration : 15 jours maximum, avec certificat médical initial.</p>
    <p><strong>Maladie professionnelle :</strong> maladie reconnue comme liée au travail. Délai de déclaration : 2 ans à partir de la première constatation médicale, ou à partir du lien établi avec l'activité professionnelle.</p>
    <div class="fei-note">Besoin d'aide pour un arrêt contesté ou une procédure ? Contactez la permanence CGT.</div>
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
